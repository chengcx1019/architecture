在线数据导出：线上数据哪些是可用的，哪些是需要处理替换的

![image-20190409180222298](/Users/changxin.cheng/Library/Application Support/typora-user-images/image-20190409180222298.png)

New:

data/minimize_example/helper/experiment.json

data/minimize_example/staff_distribution/staff_bind_tool.json

data/minimize_example/staff_distribution/tool.json

data/minimize_example/system_config/custom_config.json

Delete:

data/minimize_example/staff_distribution/staff_tool.json

data/minimize_example/staff_distribution/staff_tool_record.json

Staff_tool不需要插入，staff_tool_record.json命名为staff_bind_tool.json且不用插入数据库中

转化为标准输入格式

init_vehicle 删除



![image-20190409185421796](/Users/changxin.cheng/Library/Application Support/typora-user-images/image-20190409185421796.png)

data/raw_data/registered_resource/account_cellphone_counter.json                                                 |     3 +

 data/{resource_pool/account_data => raw_data/registered_resource/ok}/staff.json                                  |     0

 data/raw_data/registered_resource/ok/staff_counter.json                                                          |     4 +

 data/{resource_pool/account_data => raw_data/registered_resource/user_vehicle}/user.json                         |     0

 data/raw_data/registered_resource/user_vehicle/user_counter.json                                                 |     4 +

 data/raw_data/registered_resource/user_vehicle/vehicle.json                                                      |     1 +

 data/{resource_pool/vehicle_data/counter.json => raw_data/registered_resource/user_vehicle/vehicle_counter.json} |     0

 data/resource_pool/vehicle_data/vehicle.json                                                                     | 35314 ---------------------------------------------------------------

 8 files changed, 12 insertions(+), 35314 deletions(-)

 create mode 100644 data/raw_data/registered_resource/account_cellphone_counter.json

 rename data/{resource_pool/account_data => raw_data/registered_resource/ok}/staff.json (100%)

 create mode 100644 data/raw_data/registered_resource/ok/staff_counter.json

 rename data/{resource_pool/account_data => raw_data/registered_resource/user_vehicle}/user.json (100%)

 create mode 100644 data/raw_data/registered_resource/user_vehicle/user_counter.json

 create mode 100644 data/raw_data/registered_resource/user_vehicle/vehicle.json

 rename data/{resource_pool/vehicle_data/counter.json => raw_data/registered_resource/user_vehicle/vehicle_counter.json} (100%)

 delete mode 100644 data/resource_pool/vehicle_data/vehicle.json



环境初始化

