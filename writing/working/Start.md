[TOC]

## 远程服务登录

go:gdb {env} {project}

go {ip}

## Spring boot

围绕主要的语言生态打造一套标准化的微服务交付体系：java，python

IoC

AOP

借助于Spring框架原有的一个工具类：SpringFactoriesLoader的支持，@EnableAutoConfiguration可以“智能”地自动配置功效才得以大功告成！

### spring-boot源码编译

参考[IDEA 编译运行 Spring Boot 2.0 源码](https://my.oschina.net/dabird/blog/1942112)

在spring-boot根目录运行`mvn -Dmaven.test.failure.ignore=true -Dmaven.test.skip=true clean install`;



### spring-boot启动流程



### 热加载

在pom文件中添加

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>springloaded</artifactId>
    <version>1.2.4.RELEASE</version>
</dependency>


```

### Spring Boot + Cassandra

在pom.xml中加入依赖

```

```





## 从零开始构建tibbers

### 目前热加载的配置

[热加载配置修改](https://www.jianshu.com/p/6b8cffa252c0)

- 在pom.xml中添加依赖

  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-devtools</artifactId>
      <optional>true</optional>
  </dependency>
  
  ```

- 系统设置中修改compiler，勾选上build project automatically

- 注册comand + shift + option + / 打开Maintenance窗口，勾选compiler.automake.allow.when.app.running

勾选后面两项也不会在保存后自动编译，因为在mac系统里需要手动执行编译，因而取消这两项配置。

https://github.com/spring-projects/spring-loaded

## maven

https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

```shell
mvn archetype:generate
mvn clean -U package
mvn spring-boot:run

https://confluence.nevint.com/pages/viewpage.action?pageId=136874545&src=contextnavpagetreemode
```

### know maven

> 全面的了解maven

#### maven basics

groupId：组织名com.nio.swc.sas

artifactId：project

```shell
mvn -B archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.nio.swc.sas -DartifactId=maven-app
```

##### 关于pom.xml

> POM stands for Project Object Model

<version>通常含snaphsot字样表明正在开发中或者是不稳定的版本

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>1.5.9.RELEASE</version>
</parent>
```

在super pom中还有许多配置，具体的配置内容可以参考文档https://maven.apache.org/guides/introduction/introduction-to-the-pom.html

通常一个项目中会有多个mudule，比如这样的结构：

```shell
|-- my-module
|   `-- pom.xml
`-- pom.xml
```

那么如果需要在子模块中引入整个项目的pom.xml,在my-module/pom.xml中加入以下配置：

```xml
<project>
  <parent>
    <groupId>com.mycompany.app</groupId>
    <artifactId>my-app</artifactId>
    <version>1</version>
  </parent>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-module</artifactId>
  <version>1</version>
</project>
```



#### maven plugins

进行一些额外的配置，比如设置编译器的版本

```xml
<build>
  <plugins>
     <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.0</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
  <plugins>
</build>
```



#### maven dependencies

如果引入依赖A，而A依赖于B，B依赖于C，你只需要引入A，maven会帮助你管理获取其他的依赖

dependencies和dependencyManagement的[区别](http://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)：

parent pom的\<dependencies>标签中的依赖会全部被child pom继承，而\<dependencyManagement>中的依赖只有出现在chile pom的\<dependencies>中才会被包含进子模块。dependencyManagement可以集中管理依赖的版本，之后在子模块child pom的\<dependencies>中进行引用就不需要指定版本，但仍需要在child pom的\<dependencies>中引入该依赖。

#### maven build lifecycle

lifecycle：

- default

- Clean

- Site

phase：

- validate: 检查项目所需的必要信息是否可用
- compile: 编译源文件，在执行`mvn compile`之后，所有编译的文件会存储在target文件夹中
- test：运行项目中所有的单元测试（项目中会添加Junit依赖）
- package:运行上面的3个指令后打包项目
- verify:确认项目满足质量标准
- install:在本地仓库中安装package
- deploy:将package部署到远程仓库
- clean:删除target目录中的所有内容

**reference**

https://medium.freecodecamp.org/how-to-get-started-with-maven-36851d8cfd96

https://maven.apache.org/guides/introduction/introduction-to-the-pom.html

http://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html



## java

反射，

##### 基础类型默认值

| Type    | default  |
| ------- | -------- |
| boolean | flase    |
| char    | null     |
| byte    | (byte)0  |
| short   | (short)0 |
| int     | 0        |
| long    | 0L       |
| float   | 0.0f     |
| double  | 0.0d     |

### 泛型

泛型类

泛型方法

边界符

统配符

PECS原则

类型擦除

### 面向对象

实例与类型

缺省的对象比较:

```java
 public boolean equals(Object obj) {  
    return (this == obj);  
}  
```

java创建对象的几种方式：

1. 用new语句创建
2. 运用反射手段，调用java.lang.Class或者java.lang.reflect.Constructor类的newInstance()实例方法
3. 调用对象的clone()方法
4. 运用反序列化手段，调用java.io.ObjectInputStream对象的readObject()方法。

1和2都会明确的、显示的调用构造函数，3是对内存中已有对象的复制，因而不会调用构造函数，4是从文件中还原对象，因而也不会调用构造函数。

### 集合类

- collection
  - List
    - ArrayList
    - LinkedList
    - Vector
  - Set
    - HashSet：散列函数
    - TreeSet：红黑树
    - LinkedHashSet：链表结合散列函数
  - Queue
    - PriorityQueue

-  map
  - HashMap
  - HashTable
  - TreeMap



### 多态

多态性可以简单地概括为“一个接口，多种方法”，在程序的运行过程中才决定调用哪种方法。多态性是面向对象编程领域的核心概念。

简单来讲，就是一句话：允许将子类类型的指针赋值给父类类型的指针。

> 多态性在Object Pascal和C++中都是通过**虚函数**实现的。虚函数就是允许被其子类重新定义的成员函数。子类重新定义父类虚函数的做法被称为“覆盖”，或者被称为“重写”。重载与重写不同，重载是指允许存在多个同名函数，而这些函数的参数表不同（或许参数的个数不同，或许参数类型不同，或许两者都不同）。重载只是一种语言特性，与多态无关，也与面向对象无关。函数的重载是与返回值无关的。



### 继承和接口

继承会破会封装性，因而有人提出更多使用组合来完成新功能，在基于对象组合进行设计的系统中，会有更多的对象、更少的类，系统的行为将由对象间的交互来决定。

如通过array来实现queue可以有来两种方式：

继承方式

```java
class Queue extends Array {
    //etc...
}
```

或对象组合方式

```java
class Queue extends Object {
    private Aarray anArray;
    //etc...
}
```



#### 不能继承的情况

匿名内部类是没有名字的内部类，不能extends其他类，但一个内部类可以作为一个接口，由另一个内部类实现。

#### 抽象类与接口

**抽象类**

1. 抽象类只能作为其他类的基类，它不能直接被实例化，而且对抽象类不能使用new操作符。
2. 抽象类允许包含抽象成员，但这不是必须的；允许一个抽象类中没有抽象成员；允许抽象类中可以有非抽象方法。
3. 抽象类不能同时又是final的，因为抽象类总是希望被继承的，不能没有存在的。
4. 如果一个非抽象类从抽象类中派生，则其必须通过覆盖来实现所有继承而来的抽象成员。
5. 抽象类可以被抽象类所继承，结果仍是抽象类。
6. 抽象类允许被申明。

**接口**

> 接口提供更高的抽象级别，提供统一的协议；变化的东西不能出现在接口中，接口只是对一类事物的属性和行为更高层次的抽象，对修改关闭，对扩展开放。

1. 接口用于描述系统对外提供的所有服务，因此接口中的成员变量和方法必须是public类型的，确保外部使用者能访问它们。
2. 接口仅仅描述系统能做什么，但不指明如何去做，所以接口中的方法都是抽象abstract的。
3. 接口不涉及和任何具体实例相关的细节，因此接口没有构造方法，不能被实例化，没有实例变量，只有静态变量。
4. 接口中的变量是所有实现类共有的，所以变量需要用final修饰。
5. 接口中不可以出现变量。

接口属性的修饰默认是public static final，且必须赋初值；接口方法的默认属性是public abstract。

### 设计模式



### 深入理解java虚拟机

java内存区域与内存溢出异常

运行时数据区域：



程序计数器

虚拟机栈

本地方法栈

java堆

方法区

运行时常量池







## idea

### 各系统启动参数

- one cloud

  ```
  VM Option:
  -DLog4jContextSelector=org.apache.logging.log4j.core.async.AsyncLoggerContextSelector         
  ```

  ```
  Program Arguments:
  --spring.active.profiles=dev --spring.cloud.consul.enabled=false
  ```

- tibbers

  ```
  VM Option:
  -Dspring.profiles.active=dev -Dtibbers.consul=false
  ```

- power house

  

### 服务器

修改pom文件，使用jetty代替tomcat

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jetty</artifactId>
</dependency>
```





### lombok

- @Data

  自动生成默认构造方法

  自动生成所有属性的set和get方法

  还会生成equals，canEqual，hashCode，toString方法

- @Setter

  注解在 **属性**上；为单个属性提供 set 方法; 注解在 **类** 上，为该类所有的属性提供 set 方法， 都提供默认构造方法。

- @Getter

  注解在 **属性**上；为单个属性提供 get 方法; 注解在 **类** 上，为该类所有的属性提供 get 方法， 都提供默认构造方法。

- @Log4j

  注解在 **类** 上；为类提供一个 属性名为 log 的 log4j 日志对象，提供默认构造方法。

- @AllArgsConstructor

  注解在 **类** 上；为类提供一个全参的构造方法，加了这个注解后，类中不提供默认构造方法了。

- @NoArgsConstructor

  注解在**类**上；为类提供一个无参的构造方法。

- @EqualsAndHashCode

  注解在**类**上, 可以生成 equals、canEqual、hashCode 方法。

- @NonNull

  注解在**属性**上，会自动产生一个关于此参数的非空检查，如果参数为空，则抛出一个空指针异常，也会有一个默认的无参构造方法。

- @Cleanup

  这个注解用在 **变量** 前面，可以保证此变量代表的资源会被自动关闭，默认是调用资源的 close() 方法，如果该资源有其它关闭方法，可使用@Cleanup(“methodName”) 来指定要调用的方法，也会生成默认的构造方法

- @ToString

  这个注解用在**类**上，可以生成所有参数的toString方法，还会生成默认的构造方法。

  ```java
  import lombok.ToString
  @ToString
  public class Message {
      private Long id;
      private String msg;
      private Date sendTime;
  }
  ```

  等价于

  ```java
  public class Message {
      private Long id;
      private String msg;
      private Date sendTime;
      
      public Message() {
      }
      
      public String toString() {
          return "Message(id=" + this.id + ", msg=" + this.message + ", sendTime=" + this.sendTime + ")";
      } 
  }
  
  ```

  

- @RequiredArgsConstructor

  这个注解用在**类**上，使用类中所有带有@NonNull注解的或者带有final修饰的成员变量生成对应的构造方法。

- @Value

  这个注解用在 **类** 上，会生成含所有参数的构造方法，get 方法，此外还提供了equals、hashCode、toString 方法。

- @SneakyThrows

  这个注解用在 **方法** 上，可以将方法中的代码用 try-catch 语句包裹起来，捕获异常并在 catch 中用 Lombok.sneakyThrow(e) 把异常抛出，可以使用 @SneakyThrows(Exception.class) 的形式指定抛出哪种异常，也会生成默认的构造方法。

- @Synchronized

  这个注解用在 **类方法** 或者 **实例方法** 上，效果和 synchronized 关键字相同，区别在于锁对象不同，对于类方法和实例方法，synchronized 关键字的锁对象分别是类的 class 对象和 this 对象，而 @Synchronized 的锁对象分别是 私有静态 final 对象 lock 和 私有 final 对象 lock，当然，也可以自己指定锁对象，此外也提供默认的构造方法。





## 结构

## 其他

[编码规范](https://confluence.nevint.com/pages/viewpage.action?pageId=25764287)

## reference