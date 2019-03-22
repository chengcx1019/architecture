#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin.cheng
@mail: chengcx1019@gmail.com
@file: parse_html.py
@time: 2019-03-11 14:29
"""
import json
import os
from time import strftime

import requests
from lxml import html

project_start_page = {
    'nsc': '6091',
    '135': '7518',  # power-house
    '386': '14426',  # morgan
    '149': '4679',  # tibbers
    'banker': '15934',
    'autoInsert': '15804',
    '405': '15566',  # inspector
    '289': '11629',  # pipes
    '165': '11628',  # microscope
    '375': '14105',  # autopedia
}

project_show_name = {
    'nsc': 'nsc',
    '135': 'power-house',
    '386': 'morgan',
    '149': 'tibbers',
    'banker': 'banker',
    'autoInsert': 'autoInsert',
    '405': 'inspector',
    '289': 'pipes',
    '165': 'microscope',
    '375': 'autopedia',  # autopedia
}

project_notice_url = {
    'nsc': 'http://showdoc.nevint.com/index.php?s=/nsc&page_id=6091',
    '135': 'http://showdoc.nevint.com/index.php?s=/135&page_id=7518',  # power-house
    '386': 'http://showdoc.nevint.com/index.php?s=/386&page_id=15490',  # morgan
    '149': 'http://showdoc.nevint.com/index.php?s=/149&page_id=4679',  # tibbers
    'banker': 'http://showdoc.nevint.com/index.php?s=/banker&page_id=15934',
    'autoInsert': 'http://showdoc.nevint.com/index.php?s=/autoInsert&page_id=15807',
    '405': 'http://showdoc.nevint.com/index.php?s=/405&page_id=15566',  # inspector
    '289': 'http://showdoc.nevint.com/index.php?s=/289&page_id=11629',  # pipes
    '165': 'http://showdoc.nevint.com/index.php?s=/165&page_id=11628',  # microscope
    '375': 'http://showdoc.nevint.com/index.php?s=/375&page_id=14105',  # autopedia
}

notice = '#### Note\n 请先阅读 [ {project} 接入须知]({notice_url} "接入须知") ' \
         '再开始后续的系统接入工作。  \n  \n  '

cookies = {'PHPSESSID': 'a80jufj14i84vs78n2laer3i87', 'cookie_token': '0984bd4a1514dce086b5d01658e781a9'}

path = os.path.dirname(os.path.abspath('__file__'))

batch_list = ['375']


def main():
    for project, start_page in project_start_page.items():
        if project in batch_list:
            print('{project} start'.format(project=project))
            parse(project, project_start_page.get(project), cookies)
            print('{project} end'.format(project=project))


def parse(project, start_page, cookies):
    start_url = 'http://showdoc.nevint.com/index.php?s=/{project}&page_id={start_page}'.format(project=project,
                                                                                               start_page=start_page)
    r = requests.get(start_url, cookies=cookies)
    # r.content.decode()
    tree = html.fromstring(r.content)
    li_list = tree.xpath(
        '//body/div[@class="doc-body row"]/div[@class="doc-left span3 bs-docs-sidebar pull-left"]/ul[@class="nav '
        'nav-list bs-docs-sidenav"]/li')
    if len(li_list) > 0:
        hrefs = li_list[0].xpath('//@href')
        # print(hrefs)
        real_docs = list(filter(lambda x: x.startswith('/index.php?s=/home/page/index/page_id/'), hrefs))
        print(real_docs)
        date_now = strftime("%Y%m%d")
        f = open(os.path.join(path, 'log', project_show_name.get(project) + date_now + '.txt'), 'w+')
        for doc_edit in map(change_index_edit, real_docs):
            try:
                print('{project} page {page} start...'.format(project=project_show_name.get(project), page=doc_edit))
                f.write('{project} page {page} start...'.format(project=project_show_name.get(project), page=doc_edit))
                f.write('\n')
                post_data = get_post_data(doc_edit, cookies)
                # print(post_data)
                build_notice(project, post_data)
                # print(post_data)

                save_show_doc(post_data, cookies)
                # break
            except Exception as e:
                print('{project} page {page} error...'.format(project=project, page=doc_edit))
                print(e)
        f.close()


def build_notice(project, post_data):
    project_notice = notice.format(project=project_show_name.get(project, ""),
                                   notice_url=project_notice_url.get(project, ""))
    post_data['page_content'] = project_notice + '\n' + post_data['page_content']


def change_index_edit(url):
    doc_index = url.split('/')
    doc_index[4] = doc_index[4].replace('index', 'edit')
    return '/'.join(doc_index)


def get_post_data(doc_edit, cookies):
    post_data = dict()
    url = 'http://showdoc.nevint.com{doc}'.format(doc=doc_edit)
    edit_r = requests.get(url, cookies=cookies)
    tree = html.fromstring(edit_r.content)
    edit_left_head = tree.xpath(
        '//body/div[@id="layout"]/header[@class="row"]/div[@class="head-left  pull-left"]/ul[@class="inline"]/li')

    default_second_cat_id = 0
    default_child_cat_id = 0
    cat_id = default_second_cat_id
    parent_cat_id = default_child_cat_id
    try:
        default_second_cat_id = int(tree.xpath('//body/div[@id="layout"]/input[@id="default_second_cat_id"]')[
                                        0].value)
        cat_id = default_second_cat_id
    except Exception as e:
        print("default_second_cat_id: ", e)

    try:
        default_child_cat_id = int(tree.xpath('//body/div[@id="layout"]/input[@id="default_child_cat_id"]')[
                                       0].value)
        parent_cat_id = default_child_cat_id
    except Exception as e:
        print("default_child_cat_id", e)

    if parent_cat_id > 0:
        cat_id = parent_cat_id

    post_data['cat_id'] = cat_id

    post_data['page_id'] = tree.xpath('//body/div[@id="layout"]/input[@id="page_id"]')[0].value
    "cat_id"
    """
    cat_id = default_second_cat_id 
    parent_cat_id = default_child_cat_id
    """
    post_data['cat_id'] = cat_id
    post_data['s_number'] = edit_left_head[0].xpath('//input')[3].value
    post_data['page_content'] = tree.xpath('//body/div[@id="layout"]//textarea[@id="page_content"]/text()')[0]
    post_data['page_title'] = edit_left_head[0].xpath('//input')[0].value
    post_data['page_comments'] = tree.xpath('//body/div[@id="layout"]/input[@id="page_comments"]')[0].value
    post_data['item_id'] = tree.xpath('//body/div[@id="layout"]/input[@id="item_id"]')[0].value

    return post_data


def get_cat(item_id, cookies):
    r = requests.post("http://showdoc.nevint.com/index.php?s=home/catalog/secondCatList",
                      data={'item_id': item_id},
                      cookies=cookies)
    data = json.loads(r.text)
    if data.get("error_code") == 0:
        cat_list = data.get("data")


def get_cat_child(default_second_cat_id, cookies):
    r = requests.post("http://showdoc.nevint.com/index.php?s=home/catalog/childCatList",
                      data={"cat_id": default_second_cat_id},
                      cookies=cookies)
    data = json.loads(r.text)
    if data.get("error_code") == 0:
        cat_list = data.get("data")


def save_show_doc(post_data, cookies):
    r = requests.post("http://showdoc.nevint.com/index.php?s=home/page/save",
                      data=post_data,
                      cookies=cookies)


if __name__ == '__main__':
    main()
