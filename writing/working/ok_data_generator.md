### 自定义构造 staff_distribution

1. 核心数据集：staff   arrangement    staff_tool_record

2. 构造辅助数据集：
+ position / staff_group
+ staff
    * staff_skill
    * staff_job
    * staff_group_city
+ arrangement
    * arrangement_business_tool    （pm、ps,ps默认绑定）
    * arrangement_city
    * position
+ 静态数据
    * business
    * business_job
    * business_skill
    * business_tool
    * config
+ staff_tool_record 排班与工具的绑定（工具车、移动充电车、换电站）


{
       "staff": "1543596610",       已有
       "external": "09634",        工号，不必要
       "phone": 13011111174,       已有
       "group": "144",               ❎
       "en_name": "Longfei ZHAO",
       "account": "2132546679",    同 staff
       "status": 0,               default
       "inst_arrangement": 0,       default
       "inst_appointment": 0,   default
       "is_busy": 0,            default
       "is_delete": 0,          default
       "schedule_item": 0       default
}

{
    "group": "144",
    "city": "\u5317\u4eac\u5e02 - \u5317\u4eac\u5e02",
    "city_code": "110100",
    "name": "\u5317\u4eac\u8fd0\u8425-\u7f8e\u51ef\u9f9910\u70b9\u7ec4",
    "work_day": "6",       delete
    "rest_day": "1",         delete
    "unlimited_tools": "tool_vehicle,power_mobile",  default:tool_vehicle,power_mobile
    "status": "0",
    "is_auto_arrange": "0",     delete
    "is_auto_onduty": "0",      default
    "duty_position": "248",     默认上下班的位置，default，在排班中指定
    "recharge_position": "249"
}

{
    "position": "249",
    "resource": "144",        组 id
    "latitude": "39.929200",
    "longitude": "116.545400",
    "city": "\u5317\u4eac\u5e02 - \u5317\u4eac\u5e02 - \u671d\u9633\u533a",
    "city_code": "110105",
    "name": "\u767d\u5bb6\u697c\u5c0f\u533a\u5145\u7535\u7ad9",
    "address": "\u5317\u4eac\u5e02\u671d\u9633\u533a\u767d\u5bb6\u697c\u5c0f\u533aA\u533a\u5317",
    "position_type": "0",        default
    "status": "-1"
}

{
  "group": "144",       拿 staff_group copy
  "city_code": "131000",
  "city": "\u6cb3\u5317\u7701 - \u5eca\u574a\u5e02"
}

staff_job
| charge_mobile     |
| charge_valet      |
| extra_staff       |
| nio_charge_mobile |
| watch             |
| x_staff


staff_skill: communication  drive_c   electrical_tech   freight


{
    "arrangement": "210256",
    "staff": "1543596610",
    "group": "144",           拿 staff_group
    "schedule_item": "224",    随便填
    "start_position": "248",  上下班位置
    "end_position": "248",
    "estimate_start_time": "2019-03-17 14:00:00",   预计上下班时间
    "estimate_end_time": "2019-03-18 02:00:00",
    "total_break_time": "0",           delete，不用填
    "remark": "",
    "is_notification_todo": "0",       delete
    "is_notification_done": "0",       delete
    "final_estimate_start_time": "2019-03-17 14:00:00",    预计上下班时间，同 estimate_start_time
    "final_estimate_end_time": "2019-03-18 02:00:00",
    "status": 0                走 default
  }

arrangement_business_tool
{
      "arrangement": "210256",
      "business_code": "communication",
      "business_type": "0",
      "tool_type": "",
      "tool": "",
      "start_time": "2019-03-17 13:29:07",  与排班中  final_estimate_start_time 一样
      "end_time": "2019-03-18 02:06:08",
      "is_active": 1  default = 0
} 表明排班能干的事情
business_type：1：job 、2：business

job 通过 staff_job 取一个，代表该排班是 ps,pm,cs,nio_charge ，分配 staff 时，在 staff_job 中指定专员类型
business_code 通过 staff_job 去 business_job 中取出多个

假如 business_type 类型是 business
需要设置 tool_type和 tool_id。tool_type 从 business_tool 中用 business_code 获取，tool_id 即专员绑定的工具

business_tool 目前一对一

arrangement_city   通过 arrangement 和 staff_group 一对一组合
{
   "arrangement": "210256",
   "city_code": "110100",
   "staff": "1543596610",
   "group": "144"
 }

 缺失 tool 数据：
 tool_type

 group_id
 status： 设置为激活

 group 不涉及调度，可以考虑放到 raw_data 。表示资源和专员的所属关系，位置可以在上下班指定。 创建一个组，以 arrangement 的 position 为上下班位置。

 config {         调度可以多占的时间，服务半径
   "config_type": "0",
   "config_key": "onduty_offset",
   "config_value": "0",
   "source_type": "2",
   "source": "144",
   "creation_time": "2019-03-17 12:13:23",
   "update_time": "2019-03-17 12:13:23"
 }