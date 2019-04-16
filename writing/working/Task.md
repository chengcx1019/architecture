[TOC]



# first sprint-114

commit 要求：

Merge branch 'sprialias

nt-112' into 'sprint-113'

bugfix: @SASU-759

feat: add republish wifi and auth @SAS-10028

# second sprint-115

查询车辆可换电标签http://showdoc.nevint.com/index.php?s=/135&page_id=7859，返回的是一个包含很多车辆标签的列表，传入vehicleId则只返回该车辆信息

```java
static class OrderDetailFunction<T> {
        Function<Order, T> getOrderPartData;
        BiConsumer<T, OrderDetailResponse> setResponse;

        static <T> OrderDetailFunction build(Function<Order, T> function, BiConsumer<T, OrderDetailResponse> consumer) {
            OrderDetailFunction orderDetailFunction = new OrderDetailFunction();
            orderDetailFunction.setResponse = consumer;
            orderDetailFunction.getOrderPartData = function;
            return orderDetailFunction;
        }

        void queryAndSet(Order order, OrderDetailResponse response) {
            T data = getOrderPartData.apply(order);
            setResponse.accept(data, response);
        }
    }

function的返回值为T，而T作为参数，被赋值给res（即OrderDetailResponse），
```

记一次无聊的赋值

```java
ImmutableMap.<String, Object>builder()
                .put("vehicle_versions", ImmutableMap.<String, Object>builder()
                        .put("pkg_software_no", pkgSoftwareNo)
                        .put("pkg_no_display", pkgNoDispaly)
                        .put("vehicle_ecu", ecuList)
                        .build())
                .put("vehicle_others", ImmutableMap.<String, Object>builder()
                        .put("nfc_supported", nfcSupported)
                        .put("swap_blacklist", swapBlack)
                        .build())
                .build();
```

lambok注解，继承实体类时重写equals方法，默认不调用super方法





可能存在的问题：

在OrderStatusChangeService -> handleOrderStatusChange -> takeVehicleStatusSnapshotIfNeeded方法中，判断是否已存快照的方法是查询同步存储的status快照是否存储成功，若存储status快照动作已实现，则默认已向powerhouse发出请求；如果不行，可以更改为请求powerhouse记录快照成功，否则统一不作存储。



#### bugfix

以下orderid无法取出版本快照

当订单长时间无人接单时，orderStatus会变为blocked





SE:skyoof.shen,jiajun.zhu

# third sprint-116

### 前言

[Banker](https://confluence.nevint.com/pages/viewpage.action?pageId=83592227)系统：目前所有面向用户的服务（Power Express/Shaman）

> shaman要解决的业务场景为：用户自驾到达充电桩进行扫码充电.

### 卡券核销：

1. 查券，核券，销券

   ```java
   /**
    * PaymentTimeOutCheckJob
    * TaskDispatchJob
    * filterByNioChargePaymentStatus()
    * RefundAction
    * 查券，核券，扣券
    * 更新费用表，订单状态
    * 支付定时任务更新
    * 退款更新
    
   
   
   //order type为内部，走原验证逻辑，type为外部验证
   //对于内部订单，订单状态是已支付或不需要支付，则均不必抵扣卡券，对于"蔚来加电"服务，由于外部订单即蔚来加电服务一直是未支付状态，
   // 只通过改变"是否需要支付"字段来判定抵扣状态，即如果不需支付则不能抵扣卡券，所以综上，沿用原验证逻辑
   // validateOrderPaymentStatus(orderId); 避免调用两次
   updateFeeInfoViaFeeType;//将订单对应的费用项设置为fee_amout,并备注使用的卡券信息
   atomicOrderFeeService//查询对应订单的所有费用信息，并求出新的总额，查询更新后订单的费用总额
   
   ```

2. 更新费用表

    

3. 支付定时任务更新

   选出支付订单为“需要支付”的订单进行支付检查

   

4. 更新可以派单的订单

   

   去除状态为未支付的外部订单中，无需支付的订单(未支付且需要支付的订单才是真正的未付订单)

5. 检查需要退款的订单

   支付状态为已支付，且需要支付订单的订单才需要退款

   `order.getPaymentStatus()==PaymentStatus.PAID.getCode()`,`order.getPaymentNeed() == false`

   或者再加上service type的验证

   而支付状态为未支付，且无需支付的订单是外部订单

   是否有可能出现无需支付且支付状态为已支付的订单呢？

PaymentTimeOutCheckJob

TaskDispatchJob

filterByNioChargePaymentStatus()

RefundAction

已支付的charge订单状态的可能性：

- 卡券抵扣完成，只变更为无需支付，却不变更为支付完成

连调测试：

需要进行回归，小程序端和nio app端都需要进行测试



### 发票

两部分兼容内容：

- 读取开票请求，缓存开票信息

  读取时信息的来源不同，数据结构不同，需要兼容两种数据类型；如果有流水号，则存储流水号【合并发票抬头信息】和费用明细，没有流水号则检查是否有抬头信息详细字段（计划以发票类型字段为校验点），如果都没有，则向app部分请求默认流水号(https://apidoc.nioint.com/project/417/interface/api/30400)

  nvoiceService.invoiceApply

  

- 确认支付信息，发起开票

  确认支付信息后，查询开票信息，根据取值兼容两种不同开票请求

  InvoiceService.invoiceConfirm，确认支付信息，发送开票信息至开票接口

  https://apidoc.nioint.com/project/417/interface/api/30637

通过businessOrderId取出记录

明细business_order_invoice_item（通过businessOrderId取出）

更新showdoc

http://showdoc.nevint.com/index.php?s=/banker&page_id=7938

增加流水号

1. 参数验证逻辑：

首先判断titleSerialNo是否为空：

- 若为空，判断invoiceType的是否为空
  - 若为空，则设置isDefaultTitleSerialNo为true
  - 若不为空，则判断类型，若类型为企业，则检查抬头信息和公司税号，若为个人，则检查抬头
- 不为空，则通过进行其他信息验证

2. 参数读取逻辑：

首先判断isDefaultTitleSerialNo：

- 若isDefaultTitleSerialNo==true，则申请默认sno号
- 否则
  - 判断titleSerialNo
    - 若不为空，存储titleSerialNo及相关信息
    - 否则走原逻辑

如果直接设置值会不会有问题？



## Fourth sprint-117

###  1. portal欠费查询

jira: [portal 欠费查询](https://jira.nevint.com/browse/SAS-10622)

confluence:[运营Portal-欠费查询（GuYue）](https://confluence.nevint.com/pages/viewpage.action?pageId=134414893)

one-cloud VehicleController(getVehicleArrearageInfo)->VehicleService(getVehicleArrearsInfo) ->VehicleService(getChargeServiceArrearsInfo)

tspClient->getBasicVehiclesAuthorizationInfo

**(无需传入user_id)**



http://showdoc.nevint.com/index.php?s=/nsc&page_id=7746

一键加电由business标记，service标记内外部加电，

###  2. NSC 项目 showdoc page 头部加入对应项目的「使用必读」 页面链接

[NSC 项目 showdoc page 头部加入对应项目的「使用必读」 页面链接](https://jira.nevint.com/browse/SAS-10627)

数据存储的post请求

```javascript
var saving = false;
  $("#save").click(function() {
    if (saving) return false;
    var page_id = $("#page_id").val();
    var item_id = $("#item_id").val();
    var page_title = $("#page_title").val();
    var page_comments = $("#page_comments").val();
    var page_content = $("#page_content").val();
    var item_id = $("#item_id").val();
    var s_number = $("#s_number").val();
    var cat_id = $("#cat_id").val();
    var parent_cat_id = $("#parent_cat_id").val();
    if (parent_cat_id > 0 ) {
      cat_id = parent_cat_id ;
    };
    saving = true;
    $.post(
      "?s=home/page/save", {
        "page_id": page_id,
        "cat_id": cat_id,
        "s_number": s_number,
        "page_content": page_content,
        "page_title": page_title,
        "page_comments": page_comments,
        "item_id": item_id
      },
      function(data) {
        if (data.error_code == 0) {
          $.bootstrapGrowl(lang["save_success"]);
          window.location.href = "?s=home/item/show&page_id=" + data.data.page_id + "&item_id=" + item_id;
        } else {
          $.bootstrapGrowl(lang["save_fail"]);

        }
        saving = false;
      },
      'json'
    )
  });
```

目录需要另外进行获取，有一个加载目录函数

edit.js

```javascript

```

### 

### 3. 托管订单加标签

https://confluence.nevint.com/pages/viewpage.action?pageId=147784243

任务详情v1:http://showdoc.nevint.com/index.php?s=/149&page_id=5020

任务详情v2:http://showdoc.nevint.com/index.php?s=/149&page_id=9706

microscope 查询时间表偏好by pid http://showdoc.nevint.com/index.php?s=/165&page_id=15262



需要获取订单状态，标示是闲时订单，

同时请求闲时时间段（起始是两个字段还是一个字段），以及闲时行车速度阈值



背景：闲时订单，在https://confluence.nevint.com/pages/viewpage.action?pageId=55841666有关于不同类型的服务模式的描述

目前通过用户app,向用户提供4种服务模式：

- 即时服务：以现在为时间起点，给用户的反馈包括取车和还车时间以及取车地点
- 预约服务：根据用户的预约时间反馈
- 服务推荐：推荐用户闲时加电，避免无电时手忙脚乱。
- 闲时服务：所谓闲时服务，是指用户一次配置，服务在闲时自动触发，配置包括闲时时间段，闲时车辆停放地点，触发闲时服务的车辆续航里程

one cloud OrderController中getOrderDetail也是以section的方式获取订单详情,

**业务执行流程**:

tibbers 校验order_source的类型是否是MICROSCOPE，并通过order_id进行查询（order_id首先会生成，但order_id不一定会有对应的task_id）

 - 如果是则向onecloud发送闲时任务详情请求（闲时信息请求失败做降级处理，查询失败返回为空值）
 - 如果不是闲时状态，同样返回，返回值timetable_preference为{}（空对象，非null）

one-cloud 建立新接口，返回闲时规则信息

​	根据biz_id(为order_id或task_id)和type需要为"timetable_preference"在extra_data表中查询preference_id（虽然取出的是一个列表，但原则上只会有order_id的一条记录，所以默认取第一条）,之后根据pid向microscope发送请求信息。【AtomicExtraDataService】

**业务执行流程-修改**

tibbers查询订单详情时带上section"timetable_preference"获取preference_id，根据biz_id(为order_id或task_id)和type需要为"timetable_preference"在onecloud:extra_data表中查询preference_id（虽然取出的是一个列表，但原则上只会有order_id的一条记录，所以默认取第一条）,之后根据pid向microscope发送请求信息。【AtomicExtraDataService】向microscope发送查询timetable_preference请求（http://showdoc.nevint.com/index.php?s=/165&page_id=15262）

**在v2中加入"timetable_preference"的section**



one-cloud OrderSource 103标示闲时加电

```java
public enum OrderSource {
    USER_APP_BACKEND(100),
    STAFF_APP_BACKEND(101),
    PORTAL(102),
    MICROSCOPE(103),
    SCMS(104),
    NIO_CHARGE_WECHAT_MINI_PROGRAM(106),
    NSC(110),
    OTHER(-1);

    private Integer code;

    public static OrderSource codeOf(Integer code) {
        return Arrays.stream(values()).filter(o -> o.getCode().equals(code)).findAny().orElse(OTHER);
    }
}

```

USER_APP_BACKEND(100),STAFF_APP_BACKEND(101),PORTAL(102),MICROSCOPE(103),SCMS(104),NIO_CHARGE_WECHAT_MINI_PROGRAM(106),NSC(110),OTHER(-1);



cherry中加配置microscope url配置



microscop  pipes autopedia. 

### 4. Sprint-118提测

https://confluence.nevint.com/pages/viewpage.action?pageId=150253499



## Fifth sprint-119





### 报警问题排查

查询报警设置http://falcon.nevint.com:8081/portal/hostgroup?q=power&mine=0

![image-20190318141907969](/Users/changxin.cheng/Library/Application Support/typora-user-images/image-20190318141907969.png)

查询到报警的设置是300ms，在takeVehicleSnapshot方法中，需要调用两次tsp接口，查询ecu-versions（查询车辆ECU版本信息 doc http://showdoc.nevint.com/index.php?s=/11&page_id=9176）和version-features（http://showdoc.nevint.com/index.php?s=/11&page_id=8852）

查了一下grafana的监控，takeVehicleSnapshot响应时间在80-420左右波动

![image-20190318144156895](/Users/changxin.cheng/Library/Application Support/typora-user-images/image-20190318144156895.png)

而对应时间段，tsp client的queryVersionFeaturesAll（其实还是要传all参数，同时还要存储车机版本号信息）的响应时间如下：

![image-20190318144746639](/Users/changxin.cheng/Library/Application Support/typora-user-images/image-20190318144746639.png)

tsp client的queryVehicleEcuVersions的响应时间如下：

![image-20190318145036054](/Users/changxin.cheng/Library/Application Support/typora-user-images/image-20190318145036054.png)

综合来看，takeVehicleSnapshot发出超时告警的请求里，是因为调用tsp接口的请求时间过长导致的。

- 查漏补缺：修复卡券抵款log提示

###  切换 SAS 下 java 项目的单元测试框架到 Jacoco

[切换 SAS 下 java 项目的单元测试框架到 Jacoco](https://jira.nevint.com/browse/SAS-10625)

jacoco github: [Jacoco](https://github.com/jacoco/jacoco)

Jacoco doc: https://www.jacoco.org/jacoco/trunk/doc/

pom 里面把 jacoco 相关的插件配置配上， cobertura 去掉

测试各项配置是否生效及验证

- 在终端执行命令`mvn help:describe -Dplugin=org.jacoco:jacoco-maven-plugin -Ddetail`可以获得jacoco的使用说明。

- 避免生成冗余聚合报告：

  [Configuring Reports](https://maven.apache.org/plugins/maven-site-plugin/examples/configuring-reports.html#Configuring Reports)

  **Note:** Many report plugins provide a parameter called `outputDirectory` or similar to specify the destination for their report outputs. This parameter is only relevant if the report plugin is run standalone, i.e. by invocation directly from the command line. In contrast, when reports are generated as part of the site, the configuration of the Maven Site Plugin will determine the effective output directory to ensure that all reports end up in a common location.

  

  [Selecting Reports from a Plugin: Configuring Report Sets](https://maven.apache.org/plugins/maven-site-plugin/examples/configuring-reports.html#Selecting_Reports_from_a_Plugin:_Configuring_Report_Sets)



如果你需要从插件中选择一部分报告或者想以不同的配置多次生成报告，就需要配置该插件下的参数\<reportSets>

```xml
<project>
    ···
<reporting>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <reportSets>
                <reportSet>
                    <reports>
                        <!-- select non-aggregate reports -->
                        <report>report</report>
                    </reports>
                </reportSet>
            </reportSets>
        </plugin>
    </plugins>
</reporting>
    ···
</project>
   
```

关于从report去除自动生成的类，excludes参数的相关说明，但是没有示例,使用标准通配符语法，report的参数意义可参考https://www.eclemma.org/jacoco/trunk/doc/report-mojo.html，但是该文档没有配置的示例。

```text
*   Match zero or more characters
**  Match zero or more directories
?   Match a single character

```

据此添加需要排除的文件夹配置，exclude的路径匹配不成功，目录排除参考https://github.com/jacoco/jacoco/issues/34

```xml
<execution>
    <id>report</id>
    <goals>
        <goal>report</goal>
    </goals>
    <configuration>
        <excludes>
            <exclude>**/dao/auto/*</exclude>
        </excludes>
    </configuration>
</execution>

```





#### 指令功能及作用周期

- check
  - 检查代码覆盖标准是否被满足
  - 绑定阶段：verify
- dump
  - 以TCP/IP的方式从一个以tcpserver模式运行的jacoco代理请求转储
  - 绑定阶段：post-integration-test
- help
  - 
- instrument
- merge
- prepare-agent
- prepare-agent-integration
- report
  - 代码覆盖报告
  - 绑定阶段：verify
- report-aggregate
- report-integration
- restore-instrumented-class

#### 各指令详解

先运行maven test，再生成jacoco report报告

- check

  - 检查代码覆盖标准是否被满足

  - 绑定阶段：verify

  - 配置下的rules项

    每个rule代表一个element，取值包括BUNDLE, PACKAGE, CLASS, SOURCEFILE or METHOD

    每个limits下可定义多个counter（包含在limit标签内），取值包括INSTRUCTION, LINE, BRANCH, COMPLEXITY, METHOD, CLASS

    ​	limit标签下定义某个特定counter的value的minimum或maximum属性，可以定义的value包括TOTALCOUNT,COVEREDCOUNT,MISSEDCOUNT,COVEREDRATIO, MISSEDRATIO

    ```xml
    <execution>
      <id>check</id>
      <goals>
        <goal>check</goal>
      </goals>
      <configuration>
        <rules>
          <rule>  <!-- requires an overall instruction coverage of 50% and no class must be missed -->
            <element>BUNDLE</element>  <!--element type-->
            <limits>  <!--可定义多个counter-->
              <limit>
                <counter>INSTRUCTION</counter>
                <value>COVEREDRATIO</value>
                <minimum>0.80</minimum>
              </limit>
              <limit>
              	<counter>CLASS</counter>
                <value>MISSEDCOUNT</value>
                <maximum>0</maximum>
              </limit>
            </limits>
          </rule>
          <rule> <!--requires a line coverage minimum of 50% for every class except test classes -->
          	<element>CLASS</element>
            <excludes>
            	<exclude>*Test</exclude>
            </excludes>
            <limits>
            	<limit>
              	<counter>LINE</counter>
                <value>COVEREDRATIO</value>
                <minimum>0.5</minimum>
              </limit>
            </limits>
          </rule>
        </rules>
      </configuration>
    </execution>
    
    
    <excludes>
      <exclude>com/nextev/sas/scheduler/dao/**/*.class</exclude>
      <exclude>com/nextev/sas/scheduler/kafka/consumer/message/*.class
      </exclude>
    </excludes>
    
    
    ```

  - verify


在pom.xml中增加配置

```xml
<jacoco.exclude-mybatis-dao>**/dao/**/*</jacoco.exclude-mybatis-dao>
<jacoco.exclude-test>**/*Test*.class</jacoco.exclude-test>
<jacoco.exclude-bean>**/bean/**/*.class</jacoco.exclude-bean>


<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.3</version>
  <configuration>
    <excludes>
      <exclude>${jacoco.exclude-mybatis-dao}</exclude>
      <exclude>${jacoco.exclude-test}</exclude>
      <exclude>${jacoco.exclude-bean}</exclude>
    </excludes>
  </configuration>
  <executions>
    <execution>
      <id>prepare-agent</id>
      <goals>
        <goal>prepare-agent</goal>
      </goals>
    </execution>
    <execution>

      <id>report</id>
      <phase>test</phase>
      <goals>
        <goal>report</goal>
      </goals>

    </execution>
    <execution>
      <id>check</id>
      <phase>test</phase>
      <goals>
        <goal>check</goal>
      </goals>
      <configuration>
        <rules>  <!--set check option later-->
          <rule>
            <element>BUNDLE</element>
            <limits>
              <limit>
                <counter>CLASS</counter>
                <value>COVEREDRATIO</value>
                <minimum>0.00</minimum>
              </limit>
            </limits>
          </rule>
        </rules>
      </configuration>
    </execution>
  </executions>
</plugin>

<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>2.16</version>
</plugin>
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-failsafe-plugin</artifactId>
  <version>2.16</version>
  <executions>
    <execution>
      <id>integration-test</id>
      <goals>
        <goal>integration-test</goal>
      </goals>
    </execution>
  </executions>
</plugin>

```

feat: change test coverity framework to jacoco @SAS-10625

类覆盖率

Powerhouse：

 - common：71 12%
 - core：365 6%

Morgan:

- 85 29%

Banker：

- core 67

Tibbers：

- 161 11%

Microscope：



Pipes：

http://venus.nioint.com/#/detailWorkflow/wf-20190320193005-Tn

Hi，金晓，morgan,power-house,banker,tibbers的sprint-119及之后的所有分支都会切到jacoco

### 运营portal-用户标签-取消

运营portal-用户标签https://confluence.nevint.com/pages/viewpage.action?pageId=127353342



## sixth sprint-120

### 车检2.0

jira: https://jira.nevint.com/browse/SAP-688

confluence: https://confluence.nevint.com/pages/viewpage.action?pageId=150247594

### simserver



### sim cloud server 

原型地址：https://m1ofd3.axshare.com/#g=1&p=%E5%AE%9E%E9%AA%8C%E8%AF%A6%E6%83%85%E9%A1%B5

show-doc地址：http://showdoc.nevint.com/index.php?s=/409&page_id=16064





- experiment
  - simulation
    - traffic
    - env
      - versions
      - configurations
    - supplies
      - staff
      - powerresource
    - **result**（什么形式）
    - significant variable
  - report(生成但不记录)
- 实验列表查询（创建人，创建日期，类型选择）
- 实验详情或仿真详情
- 报告生成
- 仿真触发
  - 开关（启用停止按钮，状态保存）
  - headless account 数据
- cicd



- 实验列表页

  分页设置

  实验类型动态获取还是写死

- 创建实验页

  - 参数设置是否需要改成{0:{},1:{},...}

- 实验详情页

  - report展示详情
  - 实验详情页是否需要删除仿真

- 仿真详情页

  城市，每一个实验只能跑一个城市吗



查询实验状态x/x

选择报告-返回可选参数

根据参数返回结果



- 获取结果属性字典表字典接口
- report-config-查询
- 根据config生成报告
- 暂停[执行中仿真回到未执行状态]

```json
mapping = {
            "order_complete_rate": "订单完成率",
            "total_order_num": "下单成功数",
            "staff_charging_per_order_duration": "平均 充/换电时长",
            "staff_service_order_distance": "平均专员移动距离",
            "new_sim_date_list": "仿真日期列表",
            "new_staff_service_duration": "道服专员预计占用时长",
            "new_arrangement_count": "专员排班数",
            "new_staff_valid_arrange_duration": "道服专员有效排班时长",
            "new_staff_valid_arrangement_rate": "排班有效率",
            "new_staff_arrange_duration": "专员排班时长",
            "new_staff_orders_pre_arrangement": "专员平均每排班做单数",
            "new_staff_valid_service_duration": "专员占用时长(以实际开始结束时间为准)",
            "new_staff_valid_rate": "专员利用率",
            "staff_arrange_duration": "专员排班时长",
            "complete_order_num": "订单完成数",
            "delayed_order_rate": "订单延误率",
            "order_success_rate": "下单成功率",
            "staff_arrange_rate": "排班利用率",
            "staff_return_vehicle_per_order_distance": "平均还车距离",
            "staff_return_vehicle_per_order_duration": "平均还车时间",
            "staff_service_order_duration": "小哥服务时长（订单侧）",
            "staff_to_parking_lot_picking_per_order_distance": "平均取车距离",
            "staff_to_parking_lot_picking_per_order_duration": "平均取车时长",
            "staff_to_service_location_per_order_duration": "平均去服务点时长",
            "staff_to_service_location_per_order_distance": "平均去服务距离",
            "total_service_option_num": "总需求量",
            "user_aware_service_per_order_duration": "用户平均感知服务时长",
            "staff_service_per_order_distance": "专员平均服务距离",
            "staff_service_per_order_duration": "专员平均服务时长",
            "new_used_arrangement_count": "使用的排班数量"
        }

[  
   {  
      "order_complete_rate":"0.96",
      "is_schedule_order_num":218.0,
      "total_order_num":218.0,
      "staff_charging_per_order_duration":"980.77",
      "staff_service_order_distance":5790529.158297662,
      "new_sim_date_list":"2019-02-21,2019-02-22",
      "staff_arrange_duration":4731540.0,
      "staff_service_order_duration":1170142.0,
      "cs_ps_staff_metric":{  
         "new_sim_date_list":"2019-02-21,2019-02-22",
         "new_staff_service_duration":1260776.0,
         "new_used_arrangement_count":50.0,
         "new_arrangement_count":64.0,
         "not_in_date_list_duration":52664.0,
         "new_staff_valid_arrange_duration":1576064.0,
         "new_staff_valid_arrangement_rate":"0.73",
         "new_staff_arrange_duration":2162864.0,
         "new_staff_orders_pre_arrangement":"2.80",
         "new_staff_valid_service_duration":961549.0,
         "new_staff_valid_rate":"0.44"
      },
      "user_aware_service_per_order_duration":"3543.87",
      "total_service_option_num":286.0,
      "is_reassign_order_num":0.0,
      "watch_staff_metric":{  
         "new_sim_date_list":"2019-02-21",
         "new_staff_service_duration":26130.0,
         "new_used_arrangement_count":2.0,
         "new_arrangement_count":22.0,
         "not_in_date_list_duration":0.0,
         "new_staff_valid_arrange_duration":86400.0,
         "new_staff_valid_arrangement_rate":"0.13",
         "new_staff_arrange_duration":658740.0,
         "new_staff_orders_pre_arrangement":"0.23",
         "new_staff_valid_service_duration":17130.0,
         "new_staff_valid_rate":"0.03"
      },
      "staff_service_duration":1170142.0,
      "staff_return_vehicle_per_order_duration":"1713.45",
      "staff_service_per_order_distance":"27705.88",
      "staff_to_service_location_per_order_duration":"849.65",
      "pm_staff_metric":{  
         "new_sim_date_list":"2019-02-21",
         "new_staff_service_duration":317295.0,
         "new_used_arrangement_count":13.0,
         "new_arrangement_count":14.0,
         "not_in_date_list_duration":32570.0,
         "new_staff_valid_arrange_duration":419570.0,
         "new_staff_valid_arrangement_rate":"0.92",
         "new_staff_arrange_duration":455570.0,
         "new_staff_orders_pre_arrangement":"2.43",
         "new_staff_valid_service_duration":266392.0,
         "new_staff_valid_rate":"0.58"
      },
      "staff_to_parking_lot_picking_per_order_distance":"8936.95",
      "is_dealyed_order_num":0.0,
      "staff_arrange_rate":"0.42",
      "test_id":"2019-03-12-14:45:06",
      "complete_order_num":209.0,
      "staff_return_vehicle_per_order_distance":"8937.30",
      "reassign_order_rate":"0.00",
      "staff_to_service_location_per_order_distance":"9831.64",
      "all_staff_metric":{  
         "new_sim_date_list":"2019-02-21,2019-02-22",
         "new_staff_service_duration":1604201.0,
         "new_used_arrangement_count":65.0,
         "new_arrangement_count":104.0,
         "not_in_date_list_duration":85234.0,
         "new_staff_valid_arrange_duration":2082034.0,
         "new_staff_valid_arrangement_rate":"0.61",
         "new_staff_arrange_duration":3439774.0,
         "new_staff_orders_pre_arrangement":"2.10",
         "new_staff_valid_service_duration":1245071.0,
         "new_staff_valid_rate":"0.36"
      },
      "user_aware_service_duration":740669.0,
      "staff_to_parking_lot_picking_per_order_duration":"918.10",
      "used_staff_arrange_count":65.0,
      "user_aware_picking_diff_per_order_duration":"6406.79",
      "delayed_order_rate":"0.00",
      "order_success_rate":"0.76",
      "staff_service_per_order_duration":"5598.77",
      "used_staff_arrange_duration":2760000.0,
      "normal_order_rate":"1.00"
   }
]

```









交互设计：

状态控制

与模拟器交互

​	

- 仿真状态更新
- 结果数据存储在cassandra
- 实验列表页需要分页器相关参数



Dev - prod

Run server



**在heileight中传入仿真名** don't care

 ![image-20190328181836259](/Users/changxin.cheng/Library/Application Support/typora-user-images/image-20190328181836259.png)

## seventh sprint-121

cicd([nsc-pedia](https://git.nevint.com/sas/nsc-pedia/blob/master/.gitlab-ci.yml))



数据准备

环境准备

sim

eval

1. env,dev
2. schema
3. adaptor
4. GoldenSet
   - resource pool
     - all
     - sample(样例小哥和车)
   - dataset
     - sample(样例可在dev形成闭环)
5. init 重构
6. simulator 重构

https://jira.nevint.com/browse/SAS-10980

https://jira.nevint.com/browse/SAS-10976

Gis, oakeeper,powerhouse

部署过程中发现一个问题：sas_powerhouae.json和sas_onecloud.json中，增加一个环境就需要添加一个配置,事实上这是之前的设计吧

```
HttpClientManager.allowedIgnoreHostVerifyEnv里添加新环境sim_test
ansinio_files/files/scripts/install.yml name: u'copy dev cert files' when 加sim_test

```



## eighth sprint-122

### sim cloud 联调

https://simcloud-test.nioint.com

根据城市生成服务选项需要先验知识,在某城市的实验订单数不能超过线上实际订单的数目

sim server部署

机器切换root用户或者使用sudo权限 sudo su -

### sim-server ui



## ninth sprint-123



### banker支付-部分退款改造

**注意**：



payment_record 表中platform_record_id 对应NioPay中的第三方交易流水号paymentNo

在payment_refund表中扩展出两个字段：退款流水号，退款金额，

Payment_detail表中扩展一个字段：支付来源（payment_method）







为应对主流变更的细节变动：

1. 确认开票接口收到开票请求时，需要校验是否有开票信息(用户支付但未发送开票请求)
   - 如果没有开票信息，则不开票
   - 有开票信息才能开票
2. 收到退款请求后，需要查询校验支付状态（payment_status）
   - 如果状态是退款中，则拒绝本次退款（目前逻辑是默认返回success）
   - 状态是其他，则进一步校验（即便是退款成功，也需要校验是否有余额未退），其实退款行为还是只会发生一次，只不过区别是全额退款还是部分退款
     - 校验退款金额，查询该支付行为下的所有退款流水之和及本次退款金额之和，与改次支付行为的支付总额的关系
       - 如果大于总额，拒绝本次退款
       - 合理请求，在payment_refund中记录当前payment_record的退款流水，根据支付来源确定发送退款的接口,相关接口请参考[show-doc](#业务相关show-doc)（支付来源的确定，由支付成功的callback返回，在此时在Payment_detail中更新来源）
         - 微信-支付宝（拉卡拉）
         - 微信小程序（通联）

#### 流程

1. 阅读源代码逻辑

2. 修改数据库表结构，记录sql

   ```sql
   --删除payment_record的refund_status字段，代码上线后再操作数据库
   
   alter TABLE payment_detail
   ADD COLUMN payment_method varchar(8) NOT NULL DEFAULT '0000' COMMENT '0000 未知来源 10微信，20支付宝，30快捷支付，40网银支付，50现金支付，60电汇，70银联，80支付宝扫码，90微信扫码,100通联支付,1000银行贷款';
   
   alter TABLE payment_refund
   ADD `amount` decimal(12,2) NOT NULL DEFAULT '0.00' COMMENT '退款金额',
   ADD  `platform_record_id` varchar(32) NOT NULL DEFAULT '' COMMENT '支付方的交易流水号, 比如 NIOPay 的交易流水号';
   
   
   
   ```

   数据库变更后，mybatis同步流程：

   1. 在generatorConfig.xml中修改数据库配置，修改为正在开发的env:sas_banker_$ENV
   2. 取消注释你需要的表
   3. 删除对应表的mapper.xml文件中，<mapper>标签内的内容

3. ~~增加~~修改退款状态枚举

   增加状态退款成功，退款失败

4. 增加退款接口

   两种接口的返回值略有不同，需要将成功返回的退款流水记录到payment_refund中

5. 校验amount金额

   每个支付方式payment_detail都可以查到对应的payment_record，根据pay_record查询payment_refund流水，统计payment_refund退款状态为成功的流水总金额和档次请求退款金额amount之和不大于payment_detail中记录的金额;

   校验通过，将amount值设置到payment_detail中作为一条退款记录，这个设置与数据payment_detail的记录不冲突，只做逻辑上的使用

6. 判断支付方式发送不同的退款请求

   注意两种不同方式请求的退款流水号的格式不同

7. 确认退款的回调

8. 支付成功的回调

9. 开票兼容

10. 退票兼容

     

    退款成功-会出现重复开票的情况吗



#### 相关show-doc

##### banker接口变更

[申请开票](http://showdoc.nevint.com/index.php?s=/banker&page_id=7938)：开票接口新增字段invoice_action_type，开票时机

[退款](http://showdoc.nevint.com/index.php?s=/banker&page_id=16751)：：退款接口新增字段amount，退款金额

[回调](http://showdoc.nevint.com/index.php?s=/home/page/edit/page_id/7933)

希乐，有两个小变动和你同步一下：一是退款接口，如果检测到状态是退款成功，之前的操作是默认返回成功，现在想改为抛出异常，提示已退款成功，返回状态码为fail，二是退款失败的回调业务方，在回调参数中增加一个参数payStatus，标示退款成功或失败

##### 调用外部接口

[微信小程序退款接口](http://showdoc.nevint.com/index.php?s=/313&page_id=14182)

[App支付退款申请](http://showdoc.nevint.com/index.php?s=/313&page_id=13705)



#### reference

[Banker schema](http://nsc-pedia.nioint.com/book/payment_system/payment_system_domain.html)

支付状态枚举：

```java
PayStatus:
WAIT_PAY((short) 0, "待支付"),
PAYING((short) 1, "支付中"),
PAY_SUCCESS((short) 2, "支付成功"),
PAY_FAILED((short) 3, "支付失败"),
REFUNDING((short) 10, "退款中"),
REFUND_SUCCESS((short) 11, "退款成功"),
REFUND_FAILED((short) 12, "退款失败");

```





