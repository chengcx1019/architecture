## 算法和数据结构

### 典例精析

- 图广度优先搜索

  - Word Ladder2

    给定起始词和终止词以及字典表,要求每次只能修改一个字符，且中间词必须出现在字典表中，求出最短路径的所有可能

    ```python
    def _findLadders(start, end, dic):
        # dic.add(end)
        def construct(wordList):
            neis = {}
            for word in wordList:
                for i in range(len(word)):
                    s = word[:i] + "*" + word[i + 1:]
                    if s not in neis:
                        neis[s] = [word]
                    else:
                        neis[s].append(word)
            return neis
    
        level = {start}  # 逐层搜索邻居
        parents = collections.defaultdict(set)
        neis = construct(dic)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for i in range(len(node)):
                    s = node[:i] + '*' + node[i + 1:]
                    neighbors = neis.get(s, [])
                    for n in neighbors:
                        if n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
            
        ret = [[end]]
        while ret and ret[0][0] != start:
            ret = [[p] + r for r in ret for p in parents[r[0]]]  # 如果不存在路径，ret=[]
        return ret
    
    ```

    - word ladder

      最短路径

      ```python
      from collections import deque, defaultdict
      class Solution(object):
          def ladderLength(self, beginWord, endWord, wordList):
              """
              :type beginWord: str
              :type endWord: str
              :type wordList: List[str]
              :rtype: int
              """
              def construct_word(word_list):
                  neighbor_list = defaultdict(list)
                  for word in word_list:
                      for i in range(len(word)):
                          s = word[:i] + '*' + word[i+1:]
                          neighbor_list[s].append(word)
                  return neighbor_list
              
              def bfs_word(beginWord, endWord, neighbor_list):
                  visited = set()
                  queue = deque()
                  
                  queue.append((beginWord, 1))
                  while queue:
                      word, step = queue.popleft()
                      if word not in visited:
                          visited.add(word)
                          if word == endWord:
                              return step
                          for i in range(len(word)):
                              s = word[:i] + '*' + word[i+1:]
                              neighbors = neighbor_list.get(s, [])
                              for neighbor in neighbors:
                                  if neighbor not in visited:
                                          queue.append((neighbor, step+1))
                  return 0
              neighbor_list = construct_word(wordList)
              return bfs_word(beginWord, endWord, neighbor_list)
      ```

- 数组和问题

  - 顺序顺时针打印m*n数组

    ```python
    def print_array(nums, m, n):
        start = 0
        result = []
        while start*2 < m and start*2 <n:
            print_circle(nums, m, n, start, result)
            start += 1
     
    def print_circle(nums, m, n, start, result):
        row = m - start*2
        col = n - start*2
        end_w = start + col - 1  # 当前循环最后一个数行索引
        end_h = start + row - 1  # 当前循环最后一个数列索引
        # left -> right
        for j in range(start, end_w+1):
            result.append(nums[start][j])
        # top -> bottom
        if start < end_h:
        	for i in range(start+1, end_h+1):
                result.append(nums[i][end_h])
        if start < end_h and start < end_w:
            for j in range(start, end_w)[::-1]:
                result.append(nums[end_h][j])
        if start < end_h -1  and start < end_w:
            for i in range(start+1, end_h)[::-1]:
                result.append(nums[i][start])
        
                
    ```

  - s2o面试题31 连续子数组的最大和

    ```python
    def max_sum(nums):
        ret = float('-inf') 
        curr = 0
        for num in nums:
            if curr < 0:
                curr = num
             else:
                curr += num
             ret = max(ret, curr)
    ```

  - 最长公共字串,输出最长子串长度并返回最长子串

    ```python
    
    ```

  - 有序数组。和为s的两个数字VS和为s的连续正数序列

    - 定义两个指针，start和end,分别当前序列的头和尾，curr记录当前序列的和，循环条件是start < (s+1)/2,否则start+end就已经会大于s了， 如果curr==s，则记录当前start和end，继续寻找，如果curr>s,从curr-start，并将头指针start后移



  ```python
  def seq_sum_s(nums, s):
      start = 1
      end = 2
      mid = (sum+1)//2
      curr = 0
      ret = []
      while start < mid:
          if curr == s:
              ret.append((start, end))
          elif curr > s:
              curr -= start
              start += 1
              continue
          end += 1
          curr += end
      return ret
  
  ```

  - 所有和为s的连续正数序列

  ```python
  def two_sum_s(nums, s, result=[]):
      found = False
      start = 0
      end = len(nums) - 1
      while start < end:
          curr = nums[start] + nums[end]
          if curr == s:
              found = True
              result.append(start)
              result.append(end)
              return found = False
          elif curr > s:
              end -= 1
          else
          	start += 1
      return found
  ```

  - 和为s的两个数

    两个指针分别记录头指针和尾指针，如果两个数满足则返回，若大于s，则尾指针后退，若小于s，则头指针前进

- 将字母按字母表位置重新排序，不能改变相同字母的相对顺序，其他字符不变

- ```python
  def is_letter(char):
      if 64 < ord(char) < 91 or 96 < ord(char) < 123:
          return True
      else:
          return False
  
  
  def sort(line):
      first = 0
      for m in range(len(line) - 1, -1, -1):
          if is_letter(line[m]):
              first = m
              break
      for k in range(len(line)):
          i = first
          for j in range(len(line) - 1, k-1, -1):
              if is_letter(line[j]):
                  if ord(line[i].lower()) < ord(line[j].lower()):
                      line[i], line[j] = line[j], line[i]
                  i = j
      return line
  ```

- 两个栈实现队列

  stack1存放队尾元素，stack2存放队首元素

  每次入队前检查stack2是否为空，不为空，则把stack2的元素都压入stack1中

  每次出队前检查stack1是否为空，不为空，将stack1中的元素压入stack2中

  ```python
  class QueueByStack(object):
      def __init__(self):
          self.stack1 = []
          self.stack2 = []
      
      def push(self, value):
          while self.stack2:
              self.stack1.append(self.stack2.pop())
          self.stack1.append(value)
      
      def pop(self):
          while self.stack1:
              self.stack2.append(self.stack1.pop())
          return self.stack2.pop() if self.stack2 else None
  ```


- 关于single numbe问题可以泛化成这样一类问题：数组中的数字都出现K次，只有一个除外，它出现了p次，且p%k != 0，那么我们需要选取m个数（k <= 2^m）来记录数组中数字的每一位状态（即统计每个数字每一位一出现的个数，由m位来记录），且需保证当每一位的计数达到K时，需要一个mask来将该位置0，该mask的取值与k有关

  **`mask = ~(y1 & y2 & ... & ym)`, where `yj = xj` if `kj = 1`, and `yj = ~xj` if `kj = 0` (`j = 1` to `m`).**

  以leetcode中三道single numbe问题进行说明：

  - k=2,p=1

    分析：2^1=2,即只需要一个32位数来记录所有数字每一位的状态,m=1,记录到2每一位自动置零，无需mask

    ```python
    def single_num1(nums: list):->int
        x1 = 0
        for item in nums:
            x1 ^=(item)
        return x1
    ```

  - k=3,p=1

    分析：2^2>=3,即需要两个32位数来记录所有数字每一位的状态,m=2，记录到3每一位需要mask置0，`mask=~(x1 & x2)`因为3的二进制表示为`11`,因为p=1，所以返回x1, 为了更具有一般性，稍后会以k=5,p=3进行说明

    ```python
    def single_num(nums: list):->int
        x1 = 0
        x2 = 0
        for item in nums:
            x2 ^= (x1 ^ item)
            x1 ^= (item)
            mask = ~(x1 & x2)  # for k= 3 0b11
            x2 = x2 & mask
            x1 = x1 & mask
        return x1  # for p=1 0b1
    ```

  - 第3题略有不同，数组中数字都出现2次，剩余两个不同的数都只出现一次

  思路是结合第一题，将这两个不同的数分到两个不同的组中

  ```python
  def _xor(nums):
      ret = 0
      for item in nums:
          ret ^= item
      return ret
  
  def single_num3(nums: list):->list
      if not nums:
          return -1
      xor = _xor(nums)
      mask = 1
      while (mask & xor) == 0:
          mask << 1
      a = 0
      b = 0
      for item in nums:
          if item & mask:
              a ^= item
          else:
              b ^= item 
      return [a, b]
     
  ```

  - k=5,p=3进一步说明m的选取及p!=1时应当返回哪个值

    因为2^3 >=5,m=3  p=3 0b011，k=5，二进制表示为0b101

    ```python
    def single_num_general(nums: list):->int
        x1 = 0
        x2 = 0
        x3 = 0
        for item in nums:
            x3 ^= (x2 & x1 & item)
            x2 ^= (x1 & item)
            x1 ^= (item)
            mask = ~(x3 & ~x2 & x1)  # for k 0b101
        	x3 &= mask
            x2 &= mask
            x1 &= mask
        return x1  # for p ob011,可以返回x1或x2, 1只能由出现p次的元素产生
    ```


- 任意序列的排列组合

很多问题其实都是要得到数字间的排列可能

组合：

```python
def group(nums: list):->list
    tmp = nums[:]
    ret = []
    for item in nums:
        ret.append([item])
        tmp.pop(0)
        for group in group(tmp):
            ret.append([item] + group)
    return ret
```

排列：

```python
def permutation(nums: list):->list
    if len(nums) == 1:
        return [nums]
    ret = []
    for index, item in enumerate(nums):
        tmp = nums[:]
        tmp.pop(index)
        for per in permutation(tmp):
            ret.append([item] + per)
    return ret
```

- 正则表达式匹配

  采用递归或动态规划$dp(i, j)$表示s[:i]和p[:j]是否匹配

  ```python
  def regular_expression_matching(s, p):->bool
      """
      s:sring
      p:pattern
      """
      mem = {}
      def dp(i, j):
          if (i, j) not in mem:
              if j == len(p):
                  ans = i == len(s)
              else:
                  first_match = i < len(s) and p[j] in {s[i], '.'}
                  if j+1 < len(p) and p[j+1] == '*':
                      ans = dp(i, j+2) or first_match and dp(i+1, j)
                  else:
                      ans = first_match and dp(i+1, j+1)
              mem[i, j] = ans
                      
          return mem[i, j]
  ```

- 栈的压入弹出序列

  ```python
  def is_pop_order(push_v, pop_v):->bool
      if not push_v or not pop_v or len(push_v) != len(pop_v):
          return False
      stack = []
      while pop_v:
          top_pop = pop_v[0]
      	if not stack and stack[-1] == top_pop:
              stack.pop()
              pop_v.pop(0)
          else:
              while push_v:
                  if push_v[0] != pop_v[-1]:
                      stack.append(push_v.pop(0))
                  else:
                      push_v.pop(0)
                      pop_v.pop(0) 
                      break
          if not push_v:
              while stack:
                  if stack.pop() != pop_v.pop(0):
                      return False
       return True
  ```


##### 递归和循环：

递归是在一个函数的内部调用这个函数自身，而循环则是通过设置计算的初始值及终止条件，在一个范围内重复运算。递归虽然简洁，但是需要更多的时间和空间资源，因而效率不如循环；另外，递归的本质就是把一个问题分解成许多个小问题。如果多个小问题存在相互重叠的部分，就存在重复计算。



通常应用动态规划解决问题时，都是用递归的思路分析问题，但由于递归分解的子问题中存在大量的重复，因此我们总是用**自下而上**的**循环**来实现代码。



##### 查找和排序

查找相对而言比较简单，不外乎顺序查找、二分查找、哈希表查找和二叉排序树查找。二分查找是必备知识点。



排序比查找要复杂一些，经常会要求比较插入排序、冒泡排序、归并排序、快速排序等不同算法的优劣，能够从额外空间消耗、平均时间复杂嘟和最差时间复杂嘟等比较有缺点。尤其对快速排序要特别精通



堆排序可视作提升的选择排序

### 排序

#### 讨论

- 稳定与否

  - 稳定：冒泡，插入，归并

- 排序算法时间复杂度

- 最坏时间复杂度是O(nlogn)的是

  |          |           |           |
  | -------- | --------- | --------- |
  | 选择排序 | shell排序 | 插入排序  |
  | 归并排序 | 快速排序  | 堆排序    |
  | 冒泡排序 | comb sort | -cocktail |



- 排序算法中，每经过一次交换产生新的逆序对的是：快排

  - 冒泡每交换一次，会减少一个逆序对，并不会产生新的逆序对。 

  - 简单插入排序，若插入到已排序序列的最后，则不会产生新的逆序对。 

  -  简单选择排序，每次将一个元素归位。无论由小到大归位，还是由大到小归位，都不会产生新的逆序对。 

  - 快排，是跳跃式交换，必然会产生新的逆序对。且不再产生逆序对时该轮终止。

- 排序算法可以分为这样几大类：交换排序（包括bubble sort， cocktail sort， comb sort, quicksort），选择排序（选择排序，堆排序），插入排序（插入排序，希尔排序），合并排序（合并排序）

|               | average                            | best                                                         | worst                                                        | 备注           |
| :------------ | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------- |
| 选择排序      | О(*n*2) comparisons, О(*n*) swaps  | О(*n*2) comparisons, О(*n*) swaps                            | О(*n*2) comparisons, О(*n*) swaps                            |                |
| shell排序     | depends on gap sequence            | O(*n* log *n*)                                               | O(n2) (worst known gap sequence)<br/>O(*n* log2*n*) (best known gap sequence) | 插入排序的改进 |
| 插入排序      | О(*n*2) comparisons, swaps         | O(*n*) comparisons, O(*1*) swaps                             | О(*n*2) comparisons, swaps                                   |                |
| 归并排序      | O(*n* log *n*)                     | O(*n* log *n*)                                               | O(*n* log *n*)                                               |                |
| 快速排序      | O(*n* log *n*)                     | O(*n* log *n*)                                               | O(*n*2)                                                      |                |
| 堆排序        | O(n\log n)                         | Best-case performance	O(n\log n) (distinct keys)<br/> O(n) (equal keys) | O(nlog n)                                                    |                |
| 冒泡排序      | О(*n*2) comparisons, О(*n*2) swaps | О(*n*) comparisons, О(*1*) swaps                             | О(*n*2) comparisons, О(*n*2) swaps                           |                |
| comb sort     |                                    |                                                              |                                                              | 冒泡排序的改进 |
| Cocktail sort |                                    |                                                              |                                                              |                |
|               |                                    |                                                              |                                                              |                |



#### 常见排序算法描述及实现

冒泡排序：重复比较相邻的两个元素，如果存在错误顺序，则交换她们的位置

```python
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
```



选择排序：找到数组中最大活着最小的数，之后将其放在排序数组的正确位置

```python
def selection_sort(nums):
    for i in range(len(nums)):
        mini = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                mini = j
        nums[i], nums[mini] = nums[mini], nums[i]
```

Shell排序：是直接选择排序的改进，选择一组gap值，则相应将间距为gap的元素分成了一组，组件元素内采用冒泡排序，直到gap为1，整个序列就排好了。

```python
def shell_sort(nums, step):
    gap = len(nums) // step
    while gap >0:
        for i in range(len(nums)-1, -1, -gap):
            maxi = i
           	for j in range(i, -1, -gap):
                if nums[j] > nums[maxi]:
                    maxi = j
        	nums[i], nums[maxi] = nums[maxi], nums[i]
        gap = gap // step
```



插入排序：从第二个数字开始依次与前面排好序的子数组序列进行比较

```python
def insert_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                tmp = nums[i]
                nums[j+1, i+1] = nums[j:i]
                nums[j] = tmp
```

归并排序：将数组均分成两个子数组，对每一半都进行排序，之后合并

```python
def _merge(left, right)
	l = 0
    r = 0
    ret = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
    while l < len(left):
        ret.append(left[l])
        l += 1
    while r < len(right):
        ret.append(right[r])
        r += 1
    return ret

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return _merge(left, right)
    
```



快速排序：相比归并排序，快排降低了空间复杂度，并且没有使用辅助空间。选择一个轴pivot，左边的元素比轴小，右边的元素比轴大。

通常我们使用数组的第一个元素为轴。

```python
def partition(nums, start, end):
    position = start + 1
    pivot_pos = start
    for j in range(start+1, end+1):
        if nums[j] < nums[pivot_pos]:
            nums[position], nums[j] = nums[j], nums[position]
            position += 1
    position -= 1  # 定位最后一个比pivot要小的数
    nums[position], nums[pivot] = nums[pivot], nums[position]
    return position

def quick_sort(nums, start, end):
    if start < end:
        pivot_pos = partition(nums, start, end)
        quick_sort(nums, start, pivot_pos-1)
        quick_sort(pivot_pos+1, start, end)
```



**reference**

https://www.hackerearth.com/zh/practice/notes/sorting-code-monk/

[9种排序算法的可视化及比较](http://k.sina.com.cn/article_1715118170_m663aa05a001002qyc.html)









### 树

> 一般指二叉树，由于树的结构特殊，所以基本树的算法都采用递归的方式实现，起始递归的实现方式只是分治思想的一种体现，因为关于树的很多问题其实都是可以相应的分解成类似的子问题。
>
> 如果子问题存在重复的计算过程，可以采用后序遍历的方式，自底向上的进行实现，例如判断一棵树是不是平衡的。
>
> 针对每一个递归问题的描述，作这样一个约定
>
> - 问题是如何分解成相同的一系列子问题
> - 递归结束条件



#### 树的表示

数组（list）

类

- 节点和度的关系

  节点树=总度数+1，除根节点外，每个节点都对应一个父节点的度，因而叶子节点数=总度数+1-带度节点数

- 二叉树度为2的节点和叶子节点的关系：

  `2*n2+n1+1 = n2+n1+n0` -> `n2+1=n0`



#### 树的遍历

深度优先

广度优先（从底向上逐层顺序输出树节点）

前中后序遍历的循环及递归算法实现

- Trie,前缀树

#### 二叉搜索树BST

> 二叉搜索树的中序遍历即对应顺序的数组

- 判断一棵树是否是二叉树

#### 线段树（segment tree)

是一棵完全二叉树

线段树应该支持的操作包括**updata**和**query**

- update

  更新输入数组中的某一个元素并对线段树做相应的改变。

  当输入数组中位于`i`位置的元素被更新时，我们只需从这一元素对应的叶子结点开始，沿二叉树的路径向上更新至更结点即可。显然，这一过程是一个`O(logn)`的操作。

- query

  用来查询某一区间对应的信息（如最大值，最小值，区间和等）

#### 平衡树

核心为四种旋转操作

- Left Rotation:左旋,右子树右子节点（均无论左右）

- Right Rotation:右旋,左子树左子节点

- Left-Right Rotation:先左旋再右旋,左子树右子节点

- Right-Left Rotation:先右旋再左旋,右子树左子节点

  话不多说，让我们用代码实现吧，我们将实现各种操作的代码定义在AVLNode中，node中包含4个主要变量,value,left,right和height

  ```python
  class AVLNode(object):
      """
      一旦节点的左右子树发生变更，就需要重新计算height，需要重新计算的节点的子树都不存在节点插入的情况，
      因而只要根据左右子树的高度就能计算出该节点的高度，使用compute_height()方法，但是在新节点的插入过程中，存在子树节点的变化
      """
  
      def __init__(self, value):
          self.value = value
          self.left = None
          self.right = None
          self.height = 0
  
      # 节点插入左子树左子节点
      def rotate_right(self):
          new_root = self.left
          self.left = new_root.right
          new_root.right = self
  
          # new_root会在外部重新计算高度，需要调整高度的只有当前节点self，
          self.compute_height()
  
          return new_root
  
      # 节点插入右子树右子节点
      def rotate_left(self):
          new_root = self.right
          self.right = new_root.left
          new_root.left = self
  
          # new_root会在外部重新计算高度，需要调整高度的只有当前节点self
          self.compute_height()
  
          return new_root
  
      # 节点插入左子树右子节点
      def rotate_left_right(self):
          # 首先以self.left为轴进行左旋转，构造插入左子树左节点的形状，之后再以self为轴进行右旋转
          # 新的root节点是self.left.right
          first_root = self.left
          new_root = first_root.right
          first_root.right = new_root.left
          new_root.left = first_root
  
          self.left = new_root.right
          new_root.right = self
  
          # new_root会在外部重新计算高度，需要调整高度的有当前节点self, 和first_root
          self.compute_height()
          first_root.compute_height()
          return new_root
  
      # 节点插入右子树左节点
      def rotate_right_left(self):
          # 首先以self.right为轴进行右旋转，构造插入右子树右子节点的形状，之后再以self为轴进行右旋转
          # 新的root节点是self.right.left
          first_root = self.right
          new_root = first_root.left
          first_root.left = new_root.right
          new_root.right = first_root
  
          self.right = new_root.left
          new_root.left = self
  
          # new_root会在外部重新计算高度，需要调整高度的有当前节点self, 和first_root
          self.compute_height()
          first_root.compute_height()
          return new_root
  
      def add_subtree(self, parent, value):
          if not parent:
              return AVLNode(value)
          parent = parent.insert(value)  # 插入完成后，root可能会发生变化，因而需要重新赋值
          return parent
  
      def insert(self, value):
          """
          判断新插入节点后到底属于哪种情况：
          挂载完新节点后，从新节点的第一个父节点开始判断，该节点是否平衡，如不平衡，判断属于哪种情况的不平衡，
          根据value插入的是哪棵子树，并比较子树根节点和value的大小：
          1. 左子树left，且value < left.value: rotate_right右旋转
          2. 左子树left，且value > left.value: rotate_left_right 先左旋转，再右旋转
          3. 右子树right，且value > right.value: rotate_left右旋转
          4. 右子树right，且value < right.value: rotate_right_left 先右旋转，再左旋转
          """
          new_root = self
          if self.compare_to(value) > 0:
              self.left = self.add_subtree(self.left, value)
              if self.left.dynamic_difference() > 1:
                  if self.left.compare_to(value) >= 0:
                      new_root = self.rotate_left()
                  else:
                      new_root = self.rotate_left_right()
          else:
              self.right = self.add_subtree(self.right, value)
              if self.right.dynamic_difference() < -1:
                  if self.right.compare_to(value) < 0:
                      new_root = self.rotate_left()
                  else:
                      new_root = self.rotate_right_left()
  
          # 左右子树的height均已重新计算过
          new_root.compute_height()
          return new_root
  
      def remove_from_parent(self, parent, value):
          if parent:
              return parent.remove(value)
          return None
  
      def remove(self, value):
          """
          1. 叶节点直接删除
          2. 左右子树有一边为空，返回剩余一边
          3. 左右均不为空 删除的节点左右子树均不为空，那么用左子树最大的元素a（必为叶节点）替换被删除节点，然后递归删除a节点
          """
          new_root = self
          compare = self.compare_to(value)
          if compare == 0:
              if self.left is None:
                  return self.right
              if self.right is None:
                  return self.left
              node = self.left
              while node:
                  node = node.right
              most_left_key = node.value
              self.value = most_left_key
              self.left = self.remove_from_parent(self.left, most_left_key)
              if self.dynamic_differnece() == -2:  # 只可能左子树低于右子树
                  if self.right.dynamic_differnece() < 0:
                      new_root = self.rotate_left()
                  else:
                      new_root = self.rotate_right_left()
          elif compare < 0:
              self.right = self.remove_from_parent(self.right, value)
              if self.dynamic_difference() == 2:  # 只可能左子树高于右子树
                  if self.left.dynamic_differnece() > 0:
                      new_root = self.rotate_right()
                  else:
                      new_root = self.rotate_left_right()
          else:
              self.left = self.remove_from_parent(self.left, value)
              if self.dynamic_difference() == -2:  # 只可能左子树低于右子树
                  if self.right.dynamic_differnece() < 0:
                      new_root = self.rotate_left()
                  else:
                      new_root = self.rotate_right_left()
          new_root.compute_height()
          return new_root
  
      def compare_to(self, target):
          tag = 0
          if self.value < target:
              tag = -1
          elif self.value > target:
              tag = 1
          return tag
  
      def compute_height(self):
          height = -1
          if self.left:
              height = max(height, self.left.height)
          if self.right:
              height = max(height, self.right.height)
  
          self.height = height + 1
  
      def dynamic_height(self):
          height = -1
          if self.left:
              height = max(height, self.left.dynamic_height())
          if self.right:
              height = max(height, self.right.dynamic_height())
  
          return height + 1
  
      def compute_difference(self):
          left_target = 0
          right_target = 0
          if self.left:
              left_target = 1 + self.left.height
          if self.right:
              right_target = 1 + self.right.height
  
          return left_target - right_target
  
      def dynamic_difference(self):
          left_target = 0
          right_target = 0
          if self.left:
              left_target = 1 + self.left.dynamic_height()
          if self.right:
              right_target = 1 + self.right.dynamic_height()
  
          return left_target - right_target
  
      def assert_avl_property(self):
          if abs(self.dynamic_difference()) > 1:
              return False
          if self.left:
              if not self.assert_avl_property(self.left):
                  return False
          if self.right:
              if not self.assert_avl_property(self.right):
                  return False
  
          return True
  
      def bfs(self):
          queue = deque()
          queue.append(self)
  
          while queue:
              node = queue.popleft()
              yield node.value
              if node.left:
                  queue.append(node.left)
              if node.right:
                  queue.append(node.right)
  
  
  class AVLTree(object):
  
      def __init__(self):
          self.root = None
  
      def insert(self, value):
          if not value:
              raise TypeError("value can't be None")
          if not self.root:
              self.root = AVLNode(value)
          else:
              self.root = self.root.insert(value)
  
      def remove(self, value):
          if not value:
              raise TypeError("value can't be None")
          if self.root:
              self.root = self.root.remove(value)
  
      def __contains__(self, target):
          if not target or not self.root:
              return False
          node = self.root
          while node:
              if node.compare_to(target) > 0:
                  node = node.left
              elif node.compare_to(target) < 0:
                  node = node.right
              else:
                  return True
          return False              
  ```


#### 红黑树

#### A*树

#### B系列

核心思想都是采用二分法和数据平衡策略来提升数据查找的速度。

##### B树

又名平衡多路查找树，数据库索引技术里大量使用者B树和B+树的数据结构

一棵m阶B树的特点：

- 每个节点最多有m个子节点
- 除跟节点和叶节点外，其他节点最少有ceil(m/2)个节点（ceil向上取整）
- 跟节点有两个子节点
- 所有的叶子节点都在同一层
- 有j个孩子的非叶节点有j-1个关键码，关键码按递增顺序排列

##### B+树

B+树是B树的一个升级版，相对于B树来说B+树更充分的利用了节点的空间，让查询速度更加稳定，其速度完全接近于二分法查找。

- 非叶节点不包含关键字指针
- 叶子节点包含父节点的所有关键字信息，且包含父节点关键字记录指针（即地址），且按从小到大链接
- 根节点关键字数量与其子节点的个数相同
- 非叶节点只存关键字的索引而不存地址，所有数据地址必须到叶节点才能查询到

##### B*树

B+树的变种

- 关键字个数限制不同，B*树ceil(2/3m),B+和B一样
- 节点可以向兄弟节点转移，减少分解次数

#### 树的应用

- 将二叉搜索树转换成一个排序的双向链表

  采用二叉树的中序遍历

- 最小(大)堆

- 寻找最小公共节点

- B树是不是A树的子结构

- 根据前序遍历和中序遍历序列重建二叉树

- 判断一棵树是不是平衡

  不仅要判断根节点是否平衡，还要判断子树本身是否平衡

- 判断一个序列是不是二叉搜索树的后序遍历序列

  思路：首先根据后序遍历的特性，序列的最后一个节点是当前树（或者子树）的根节点，根据根节点寻找到左子树和右子树序列（依据左子树序列的每一个元素都小于根节点，右子树序列的每一个元素都大于根节点，一旦原则上进入了右子树序列，出现比根节点小的元素，则可断定这不是后序遍历序列），对左右子树序列进行相同判断。（PS：递归停止条件在实现里描述）

  实现：定义起始指针left=0，确定左子序列，定义右子树序列指针right=left，如果当前序列只有一个节点，则会返回true，事实上除了根节点，是不会出现空序列进入递归，单元素序列会返回true，不会进一步递归。

  ```python
  def is_post_order(order: list):
       # 事实上除了最初序列为空，递归过程中不会出现空序列进入调用的情况，在单元素就会返回了，而且一定会返回True
      if order is None or len(order) == 0: 
          return False
      root = order[-1]
      left = 0
      # 如果只有一个元素的话，不会进入循环，因而不会出现数组越界，并且 left=0，right=left，返回true
      while order[left] < root:  
          left += 1
      right = left
      while right < len(order) - 1:
          if order[right] < root:
              return False
          right += 1
      is_left = True if left == 0 else is_post_order(order[:left])  # 左子序列为空, 因而left = 0，左子满足
      is_right = True if left == right else is_post_order(order[left: right])  # 右子树为空，因而right==left，右子满足
      return is_left and is_right
  ```

- 二叉树中和为某一值的所有路径

  > 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
  >
  > 在寻找所有路径的过程自然是要使用回溯的思想

  思路：首先判断该节点是不是叶节点，累加该节点的值，如果当前路径（该节点是叶节点）的累加和和预期值一致，那么保存该路径；如果不是叶节点，或者没有达到预期值，该节点还有左子和右子，那么继续递归访问左子和右子，访问结束后，回溯到该节点的父节点（回溯的具体操作为从累加和中去除该节点的值，从 当前“路径”【不是上面明确定义的路径，而是记录从根节点一路过来访问的所有节点】中去除该节点）。

  实现：参见下方

  ```python
  def find_path(bst_root, expected_sum):
      if bst_root is None:
          return
      path = []
      current_num = 0
      self._find_path(bst_root, expected_sum, path, current_num)
  
  def _find_path(bst_root, expected_sum, path, current_sum):
      is_leaf = bst_root.left is None and bst_root.right is None
      current_sum += bst_root.data
      path.append(bst_root.data)
      if current_sum == expected_sum and is_leaf:
          print(path[:])
  
      if bst_root.left is not None:
          _find_path(bst_root.left, expected_sum, path, current_sum)
      if bst_root.right is not None:
          _find_path(bst_root.right, expected_sum, path, current_sum)
  
      # cut current node from path and current value before returning to parent
      current_sum -= bst_root.data
      path.pop()
  ```

- 字符编码最短路径

  ```python
  def shortest_hfm_tree(line):->int
      cache = {}
      for char in line:
          if char in cache:
              cache[char] += 1
          else:
              cache[char] = 0
      values =list(cache.values())
      ret = 0
      while len(values)>1:
          values.sort()
          w = values[0] + values[1]
          ret += w
          values = values[2:]
          values.append(w)
      return ret
  ```


### 图

#### 如何用图思考

[原文](https://medium.freecodecamp.org/i-dont-understand-graph-theory-1c96572a1401)



#### 图的表示

邻接数组-静态图

邻接表-动态图

邻接矩阵

#### 图的遍历

> 相比广度优先使用队列存储未访问的邻接节点，深度遍历的循环实现方式使用栈存储当前节点的未访问邻接节点

##### 广度优先搜索

广度优先搜索从边上来说，都是从源点到图中任意顶点的最短路径的最短路径

##### 深度优先搜索

顶点访问顺序会改变计数器的值，所以需要注意临接节点的顺序，深度优先搜索计算出来的结果非常有用，包括**拓扑排序**，寻找**强连通部**，寻找网络中潜在的弱点。

深度优先搜索结束后，可以使用每个顶点存储的前序节点值找到一条从**任意顶点到原点s的路径**，当然，这条路径也许不是最短路径。

深度优先搜索仅仅依靠当前信息，是一种盲目的搜索，它没有一个明智的计划来快速达到目标顶点t。

##### 深度优先搜索的应用

###### 有向无环图中的拓扑排序

###### 有向图中计算强连通分量

##### 边的分类

根据在图G上进行深度优先搜索所产生的深度优先森林

- 树边(tree edge)
- 反向边(back edge)
- 正向边(forward edge)
- 交叉边(cross edge)



#### 最短路径

有向无环图

##### 单源最短路径

###### 非负边代价（Dijkstra）

###### 任意边代价（Bellman-Ford）

不可包含总权值为负值的环

##### 任意两个顶点间最短路径

动态规划Floyd-Warshall

#### 最小生成树

给定无向连通图$G=(V,E)$

#### 关于图的其他

- 欧拉回路(不重复经过所有边)和曼哈顿回路(不重复经过所有点)
- 



### 回溯

### 位运算

位运算的主要性质：

- a^0 = a, a^a=0

位运算的应用：

- 加法 

  a&b << 1 得到进位，a^b得到各位

  循环上面的操作，直到不产生进位

- 将整数第n位置为，或者清零

- 整数最右边的1 a&(a-1)

- 将a转化为b需要反转的次数

  c = a^b，统计c中非0元素的数目

  ```python
  def flip_num(a, b):
      c = a ^ b
      count = 0
      while c:
          count += c & 1
          c = c >> 1
      return count
  ```



137  Single Number II 在一个所有数字都出现3次，只有一个数字出现一次的数组中找出这个数,可以泛化为由k,p定义的更广泛的问题

关键点是两个相同的数的异或为0， 比如A^B^A = B

###### I -- Statement of our problem

"Given an array of integers, every element appears `k` (`k > 1`) times except for one, which appears `p` times (`p >= 1, p % k != 0`). Find that single one."

###### II -- Special case with 1-bit numbers

As others pointed out, in order to apply the bitwise operations, we should rethink how integers are represented in computers -- by bits. To start, let's consider only one bit for now. Suppose we have an array of **1-bit** numbers (which can only be `0` or `1`), we'd like to count the number of `1`'s in the array such that whenever the counted number of `1` reaches a certain value, say `k`, the count returns to zero and starts over (in case you are curious, this `k` will be the same as the one in the problem statement above). To keep track of how many `1`'s we have encountered so far, we need a **counter**. Suppose the counter has `m` bits in binary form: `xm, ..., x1` (from most significant bit to least significant bit). We can conclude at least the following four properties of the counter:

1. There is an initial state of the counter, which for simplicity is zero;
2. For each input from the array, if we hit a `0`, the counter should remain unchanged;
3. For each input from the array, if we hit a `1`, the counter should increase by one;
4. In order to cover `k` counts, we require `2^m >= k`, which implies `m >= logk`.



Here is the key part: how each bit in the counter (`x1` to `xm`) changes as we are scanning the array. Note we are prompted to use bitwise operations. In order to satisfy the second property, recall what bitwise operations will not change the operand if the other operand is `0`? Yes, you got it: `x = x | 0` and `x = x ^ 0`.

Okay, we have an expression now: `x = x | i` or `x = x ^ i`, where `i` is the scanned element from the array. Which one is better? We don't know yet. So, let's just do the actual counting.

At the beginning, all bits of the counter is initialized to zero, i.e., `xm = 0, ..., x1 = 0`. Since we are gonna choose bitwise operations that guarantee all bits of the counter remain unchanged if we hit `0`'s, the counter will be `0` until we hit the first `1` in the array. After we hit the first `1`, we got: `xm = 0, ...,x2 = 0, x1 = 1`. Let's continue until we hit the second `1`, after which we have: `xm = 0, ..., x2 = 1, x1 = 0`. Note that `x1` changed from `1` to `0`. For `x1 = x1 | i`, after the second count, `x1` will still be `1`. So it's clear we should use `x1 = x1 ^ i`. What about `x2, ..., xm`? The idea is to find the condition under which `x2, ..., xm`will change their values. Take `x2` as an example. If we hit a `1` and need to change the value of `x2`, what must be the value of `x1` right before we do the change? The answer is: `x1` must be `1` otherwise we shouldn't change `x2` because changing `x1` from `0` to `1` will do the job. So `x2` will change value only if `x1` and `i`are both `1`, or mathematically, `x2 = x2 ^ (x1 & i)`. Similarly `xm` will change value only when `xm-1, ..., x1` and `i` are all `1`: **`xm = xm ^ (xm-1 & ... & x1 & i)`**. Bingo, we've found the bitwise operations!

However, you may notice that the bitwise operations found above will count from `0` until `2^m - 1`, instead of `k`. If `k < 2^m - 1`, we need some **"cutting" mechanism to reinitialize the counter to `0` when the count reaches `k**`. To this end, we apply bitwise **AND** to ` xm,..., x1`  with some variable called   `mask`, i.e., `xm = xm & mask, ..., x1 = x1 & mask`. If we can make sure that ` mask ` will be `0` only when the count reaches `k` and be `1` for all other count cases, then we are done. How do we achieve that? Try to think what distinguishes the case with ` k ` count from all other count cases. Yes, it's the count of `1`'s! For each count, we have unique values for each bit of the counter, which can be regarded as its state. If we write  k in its binary form: `km,..., k1`, we can construct    mask as follows:

**`mask = ~(y1 & y2 & ... & ym)`, where `yj = xj` if `kj = 1`, and `yj = ~xj` if `kj = 0` (`j = 1` to `m`).**

Let's do some examples:

```
`k = 3: k1 = 1, k2 = 1, mask = ~(x1 & x2)`;

k = 5: k1 = 1, k2 = 0, k3 = 1, mask = ~(x1 & ~x2 & x3);
```

In summary, our algorithm will go like this (`nums` is the input array):

```python
for i in nums:
    xm ^= (xm-1 & ... & x1 & i);
    x(m-1) ^= (xm-2 & ... & x1 & i);
    .....
    x1 ^= i;
    
    mask = ~(y1 & y2 & ... & ym) where yj = xj if kj = 1, and yj = ~xj if kj = 0 (j = 1 to m).

    xm &= mask;
    ......
    x1 &= mask;
```

###### III -- General case with 32-bit numbers

Now it's time to generalize our results from 1-bit number case to 32-bit integers. One straightforward way would be **creating `32` counters for each bit in the integer**. You've probably already seen this in other posted [solutions](https://discuss.leetcode.com/topic/455/constant-space-solution/4). However, if we take advantage of bitwise operations, we may be able to manage all the `32` counters "collectively". By saying "collectively", we mean using `m` **32-bit** integers instead of `32` **m-bit** counters, where `m` is the minimum integer that satisfies `m >= logk`. The reason is that bitwise operations apply only to each bit so operations on different bits are independent of each other (kind obvious, right?). This allows us to group the corresponding bits of the `32` counters into one 32-bit integer. Here is a schematic diagram showing how this is done.



![0_1510941016426_137. Single Number II .png](https://discuss.leetcode.com/assets/uploads/files/1510941017203-137.single-number-ii-resized.png)



The top row is the 32-bit integer, where for each bit, we have a corresponding m-bit counter (shown by the column below the upward arrow). Since bitwise operations on each of the `32` bits are independent of each other, we can group, say the `m-th` bit of all counters, into one 32-bit number (shown by the orange box). All bits in this 32-bit number (denoted as `xm`) will follow the same bitwise operations. Since each counter has `m` bits, we end up with `m` 32-bit numbers, which correspond to `x1, ..., xm` defined in part `II`, but now they are 32-bit integers instead of 1-bit numbers. Therefore, in the algorithm developed above, we just need to regard `x1`to `xm` as 32-bit integers instead of 1-bit numbers. Everything else will be the same and we are done. Easy, hum?

###### IV -- What to return

The last thing is what value we should return, or equivalently which one of `x1` to `xm` will equal the single element. To get the correct answer, we need to understand what the `m` 32-bit integers `x1` to `xm` represent. Take `x1` as an example. `x1` has `32` bits and let's label them as `r` (`r = 1` to `32`). After we are done scanning the input array, the value for the `r-th` bit of `x1` will be determined by the `r-th` bit of all the elements in the array (more specifically, suppose the total count of `1` for the `r-th` bit of all the elements in the array is `q`, `q' = q % k` and in its binary form: `q'm,...,q'1`, then by definition the `r-th` bit of `x1` will be equal to `q'1`). Now you can ask yourself this question: what does it imply if the `r-th` bit of `x1` is `1`?



The answer is to find what can contribute to this `1`. Will an element that appears `k` times contribute? No. Why? Because for an element to contribute, it has to satisfy at least two conditions at the same time: the `r-th` bit of this element is `1` and the number of appearance of this `1` is not an integer multiple of `k`. The first condition is trivial. The second comes from the fact that whenever the number of `1` hit is `k`, the counter will go back to zero, which means the corresponding bit in `x1` will be reset to `0`. For an element that appears `k` times, it's impossible to meet these two conditions simultaneously so it won't contribute. At last, only the single element which appears `p` (`p % k != 0`) times will contribute. If `p > k`, then the first `k * [p/k]` (`[p/k]`denotes the integer part of `p/k`) single elements won't contribute either. So we can always set `p' = p % k` and say the single element appears effectively `p'` times.



Let's write `p'` in its binary form: `p'm, ..., p'1` (note that `p' < k`, so it will fit into `m` bits). Here I **claim the condition** for `xj` to equal the single element is `p'j = 1` (`j = 1` to `m`), with a quick proof given below.



If the `r-th` bit of `xj` is `1`, we can safely say the `r-th` bit of the single element is also `1` (otherwise nothing can make the `r-th` bit of `xj` to be `1`). We are left to prove that if the `r-th` bit of `xj` is `0`, then the `r-th` bit of the single element can only be `0`. Just suppose in this case the `r-th` bit of the single element is `1`, let's see what will happen. At the end of the scan, this `1` will be counted `p'` times. By definition the `r-th` bit of `xj` will be equal to `p'j`, which is `1`. This contradicts with the presumption that the `r-th` bit of `xj` is `0`. Therefore we conclude the `r-th` bit of `xj` will always be the same as the `r-th` bit of the single number as long as `p'j = 1`. Since this is true for all bits in `xj` (i.e., true for `r = 1` to `32`), we conclude `xj` will equal the single element as long as `p'j = 1`.

So now it's clear what we should return. Just express `p' = p % k` in its binary form and return any of the corresponding `xj` as long as `p'j = 1`. In total, the algorithm will run in `O(n * logk)` time and `O(logk)` space.

> **Side note**: There is a general formula relating each bit of `xj` to `p'j` and each bit of the single number `s`, which is given by `(xj)_r = s_r & p'j`, with (xj)_r and `s_r` denoting respectively the `r-th` bit of `xj` and the single number `s`. From this formula, it's easy to see that `(xj)_r = s_r` if `p'j = 1`, that is, `**xj = s as long as `p'j = 1`**, as shown above. Furthermore, we have `(xj)_r = 0` if `p'j = 0`, regardless of the value of the single number, that is, `xj = 0` as long as `p'j = 0`. So in summary we obtain: `xj = s` if `p'j = 1`, and `xj = 0` if `p'j = 0`. This implies the expression (`x1 | x2 | ... | xm`) will also be evaluated to the single number `s`, since the expression will essentially take the `OR` operations of the single number with itself and some `0`s, which boils down to the single number eventually.

------

###### V -- Quick examples

Here is a list of few quick examples to show how the algorithm works (you can easily come up with other examples):



1. `k = 2, p = 1`
   `k` is `2`, then `m = 1`, we need only one 32-bit integer (`x1`) as the counter. And `2^m = k` so we do not even need a mask! A complete python program will look like:

```python
def singleNumber(nums):
	x1 = 0;
    for i in nums:
    	x1 ^= i
    return x1
```

1. k = 3, p = 1

   k is 3, then `m = 2`, we need two 32-bit integers(`x2`, `x1`) as the counter. And `2^m > k` so we do need a mask. Write `k` in its binary form: `k = '11'`, then `k1 = 1`, `k2 = 1`, so we have `mask = ~(x1 & x2)`. A complete python program will look like:

```python
def singleNumber(nums):
    """
    k=11 :影响mask
    p=1  :影响返回值
    """
	if not nums:
        return -1
    x1 = 0
    x2 = 0
    mask = 0
    for num in nums:
        x2 ^= (x1 & num)
        x1 ^= num
        mask = ~(x1 & x2)
        x2 &= mask
        x1 &= mask
   
        return x1  # Since p = 1, in binary form p = '01', then p1 = 1, so we should return x1. 
                   # If p = 2, in binary form p = '10', then p2 = 1, and we should return x2.
                   # Or alternatively we can simply return (x1 | x2).

```

1. k = 5, p = 3

   k  is  5, then m = 3, we need three 32-bit integers(`x3`, `x2`, `x1`) as the counter. And `2^m > k` so we need a mask. Write `k` in its binary form: `k = '101'`, then `k1 = 1`, `k2 = 0`, `k3 = 1`, so we have `mask = ~(x1 & ~x2 & x3)`. A complete java program will look like:

```python
def singleNumber(nums):
    """
    k=101 :影响mask
    p=011  :影响返回值
    """
	if not nums:
        return -1
    x1 = 0
    x2 = 0
    x3 = 0
    mask = 0
    for num in nums:
        x3 ^= (x2 & x1 & num)
        x2 ^= (x1 & num)
        x1 ^= num
        mask = ~(x1 & ~x2 & x3)
        x2 &= mask
        x1 &= mask
   
    return x1  # Since p = 3, in binary form p = '011', then p1 = p2 = 1, so we can return either x1 or x2. 
                   # If p = 4, in binary form p = '100', only p3 = 1, which implies we can only return x3.
                   # Or alternatively we can simply return (x1 | x2 | x3).
```



### 动态规划

- 最优二叉查找树

  - 包含n个健的二叉查找树的总数量等于第n个卡塔兰树
    $$
    当n>0时，c(n)=\cfrac{1}{n+1}[_n^{2n}],c(0)=1
    $$

    - 卡特兰数

      不能穿过对角线意味着任意时间向右的步数不能小于向左的步数，向右的步数记为左括号，向上的步数记为右括号



动态规划实质上是一种优化技术，动态规划的思想为：建立详细的最优解表。先从简单的子问题开始。通过较小问题的最优解创建越来越大问题的最优解。

#### 动态规划和分治：

动态规划是分治范式的延伸，只有当问题具有明确限制和先决条件时，才能对问题采用动态规划方法。

这两个条件是：

- 问题的最优解由子问题的最优解构成
- 问题可以被分解为子问题，这些子问题可以重复使用或者可以使用递归算法解决而不会产生新的子问题

如果满足这两个限制，那么分治问题就可以采用动态规划的方法完成。

> 二分查找是一个典型的分治问题，但二分查找没有重叠子问题，不是动态规划问题。

动态规划的两种技术(**memoization** and **tabulation**) 

- memoization

  **Memoization (top-down cache filling)** refers to the technique of caching and reusing previously computed results

  ```python
  def fib(n, mem: dict):
      if n = 0 or n = 1:
          return n
      if n not in mem:
          mem[n] = fib(n - 1, mem) + fib(n - 2, mem)
      return mum[n]
  ```

- tabulation

  **Tabulation (bottom-up cache filling)** is similar but focuses on filling the entries of the cache. Computing the values in the cache is easiest done iteratively. 

  ```python
  def fib(n, mem: dict):
      mem[0] = 0
      mem[1] = 1
      for i in range(2, n+1):
          mem[i] = mem[i-1] + mem[i-2]
      return mem[n]
  ```

  缓存有效的原因是分治问题里有重叠的子问题

  二分查找没有重叠子问题，不是动态规划问题

#### 解决动态规划问题的步骤

> [参考](http://blog.refdash.com/dynamic-programming-tutorial-example/)

- 识别动态规划问题

- 确定问题变量

- 清楚的表达递归关系

  假定已经完成了 所有的子问题之后，如何解决主要的问题，

- 确定基案本例(base case)

  不依赖任何子问题的最小子问题

  确定这个问题之前，需要想清楚主要的问题是如何简化为更小的问题，以及在什么时候问题不能被进一步简化

  问题不能被简化的原因——其中一个参数由于问题的约束，变成了一个不可能的值，即确定边界条件

- 决定是要用迭代还是递归实现

- 添加缓存（自顶向下）

- 确定时间复杂度

  有一些简单的规则可以使计算动态编程问题的计算时间复杂性容易得多

#### 典型问题

通常我们会从斐波那契数列开始谈动态规划问题，但这次为了更深入的理解动态规划，我们来点不一样的，从最小编辑距离开始看吧。

- 最小编辑距离

  首先简单描述“编辑距离”，两个字符串，将a转化成b，采用插入、删除、和替换3种变换方式，最少的变化次数称为“编辑距离”，以下问题都是将a转化成b，且矩阵a的索引i作为行标，b的索引j作为列标，那么我们可以想象，一种操作次数最长的方式就是，从尾到头删除a，再从头到尾增加b。

  实际操作过程中，我们需要保存一个决策矩阵，矩阵元素的递推关系如下：

  ![](https://camo.githubusercontent.com/384008e2a31829248d01e4375399508555a2f900/68747470733a2f2f77696b696d656469612e6f72672f6170692f726573745f76312f6d656469612f6d6174682f72656e6465722f7376672f66306134386563666339383532633034323338326664633333633139653131613136393438653835)

$$
<Empty \space Math \space Block>
$$

- 斐波那契数列及其变体青蛙跳台阶问题
- 背包问题(#jump)

#### LeetCode动态规划专题



| seq  | #                                                            |      | Title                                                        | Acceptance | Difficulty |      |
| ---- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ | ---------- | ---------- | ---- |
| 1    | <a href='#Longest Valid Parentheses'>   32</a>               |      | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) | 23.80%     | Hard       | -    |
| 2    | <a href='#Unique Paths II'>63</a>                            |      | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii) | 32.60%     | Medium     | -    |
| 3    | <a href='#Minimum Path Sum'>64</a>                           |      | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum) | 42.90%     | Medium     | -    |
| 4    | <a href='#Edit Distance'>72</a>                              |      | [Edit Distance](https://leetcode.com/problems/edit-distance) | 34.20%     | Hard       | -    |
| 5    | <a href='#Scramble String'>87</a>                            |      | [Scramble String](https://leetcode.com/problems/scramble-string) | 30.30%     | Hard       | -    |
| 6    | <a href='#Unique Binary Search Trees II'>95</a>              |      | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii) | 33.30%     | Medium     |      |
| 7    | <a href='#Interleaving String'>97</a>                        |      | [Interleaving String](https://leetcode.com/problems/interleaving-string) | 26.00%     | Hard       |      |
| 8    | <a href='#Distinct Subsequences'>115</a>                     |      | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences) | 33.10%     | Hard       |      |
| 9    | <a href='#Triangle'>120</a>                                  |      | [Triangle](https://leetcode.com/problems/triangle)           | 36.40%     | Medium     |      |
| 10   | <a href='#Best Time to Buy and Sell Stock   III'>123</a>     |      | [Best Time to Buy and Sell   Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii) | 31.40%     | Hard       |      |
| 11   | <a href='#Palindrome Partitioning II'>132</a>                |      | [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii) | 25.70%     | Hard       |      |
| 12   | <a href='#Maximum Product Subarray'>152</a>                  |      | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray) | 27.50%     | Medium     |      |
| 13   | <a href='#Best Time to Buy and Sell Stock   IV'>188</a>      |      | [Best Time to Buy and Sell   Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv) | 25.30%     | Hard       |      |
| 14   | <a href='#House Robber'>198</a>                              |      | [House Robber](https://leetcode.com/problems/house-robber)   | 40.40%     | Easy       |      |
| 15   | <a href='#House Robber II'>213</a>                           |      | [House Robber II](https://leetcode.com/problems/house-robber-ii) | 34.70%     | Medium     |      |
| 16   | <a href='#Paint House'>256</a>                               |      | [Paint House](https://leetcode.com/problems/paint-house)     | 46.90%     | Easy       |      |
| 17   | <a href='#Ugly Number II'>264</a>                            |      | [Ugly Number II](https://leetcode.com/problems/ugly-number-ii) | 34.20%     | Medium     |      |
| 18   | <a href='#Paint House II'>265</a>                            |      | [Paint House II](https://leetcode.com/problems/paint-house-ii) | 39.30%     | Hard       |      |
| 19   | <a href='#Paint Fence'>276</a>                               |      | [Paint Fence](https://leetcode.com/problems/paint-fence)     | 35.40%     | Easy       |      |
| 20   | <a href='#Perfect Squares'>279</a>                           |      | [Perfect Squares](https://leetcode.com/problems/perfect-squares) | 38.80%     | Medium     |      |
| 21   | <a href='#Longest Increasing Subsequence'>300</a>            |      | [Longest Increasing   Subsequence](https://leetcode.com/problems/longest-increasing-subsequence) | 39.30%     | Medium     |      |
| 22   | <a href='#Range Sum Query - Immutable'>303</a>               |      | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable) | 34.10%     | Easy       |      |
| 23   | <a href='#Range Sum Query 2D - Immutable'>304</a>            |      | [Range Sum Query 2D -   Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable) | 28.80%     | Medium     |      |
| 24   | <a href='#Best Time to   Buy and Sell Stock with Cooldown'>309</a> |      | [Best Time to Buy and Sell   Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) | 42.70%     | Medium     |      |
| 25   | <a href='#Create Maximum Number'>321</a>                     |      | [Create Maximum Number](https://leetcode.com/problems/create-maximum-number) | 24.90%     | Hard       |      |
| 26   | <a href='#Coin Change'>322</a>                               |      | [Coin Change](https://leetcode.com/problems/coin-change)     | 27.30%     | Medium     |      |
| 27   | <a href='#Counting Bits'>338</a>                             |      | [Counting Bits](https://leetcode.com/problems/counting-bits) | 62.90%     | Medium     |      |
| 28   | <a href='#Integer Break'>343</a>                             |      | [Integer Break](https://leetcode.com/problems/integer-break) | 46.70%     | Medium     |      |
| 29   | <a href='#Maximal Rectangle'>85</a>                          |      | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle) | 30.80%     | Hard       |      |
| 30   | <a href='#Maximal Square'>221</a>                            |      | [Maximal Square](https://leetcode.com/problems/maximal-square) | 31.20%     | Medium     |      |
| 31   | <a href='#Best Time to Buy and Sell Stock'>121</a>           |      | [Best Time to Buy and Sell   Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | 44.30%     | Easy       |      |
| 32   | <a href='#Dungeon Game'>174</a>                              |      | [Dungeon Game](https://leetcode.com/problems/dungeon-game)   | 25.20%     | Hard       |      |
| 33   | <a href='#Unique Binary Search Trees'>96</a>                 |      | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees) | 43.30%     | Medium     |      |
| 34   | <a href='#Decode Ways'>91</a>                                |      | [Decode Ways](https://leetcode.com/problems/decode-ways)     | 21.00%     | Medium     |      |
| 35   | <a href='#Regular Expression Matching'>10</a>                |      | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | 24.40%     | Hard       |      |
| 36   | <a href='#Unique Paths'>62</a>                               |      | [Unique Paths](https://leetcode.com/problems/unique-paths)   | 44.40%     | Medium     |      |
| 37   | <a href='#Maximum Subarray'>53</a>                           |      | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray) | 41.20%     | Easy       |      |
| 38   | <a href='#Climbing Stairs'>70</a>                            |      | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs) | 42.00%     | Easy       |      |
| 39   | <a href='#Word Break II'>140</a>                             |      | [Word Break II](https://leetcode.com/problems/word-break-ii) | 25.30%     | Hard       |      |
| 40   | <a href='#Russian Doll Envelopes'>354</a>                    |      | [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes) | 32.80%     | Hard       |      |
| 41   | <a href='#Android Unlock Patterns'>351</a>                   |      | [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns) | 44.70%     | Medium     |      |
| 42   | <a href='#Count Numbers with Unique   Digits'>357</a>        |      | [Count Numbers with Unique   Digits](https://leetcode.com/problems/count-numbers-with-unique-digits) | 46.20%     | Medium     |      |
| 43   | <a href='#Bomb Enemy'>361</a>                                |      | [Bomb Enemy](https://leetcode.com/problems/bomb-enemy)       | 41.20%     | Medium     |      |
| 44   | <a href='#Max Sum of Rectangle No Larger Than   K'>363</a>   |      | [Max Sum of Rectangle No   Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k) | 34.20%     | Hard       |      |
| 45   | <a href='#Largest Divisible Subset'>368</a>                  |      | [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset) | 34.00%     | Medium     |      |
| 46   | <a href='#Guess Number Higher or Lower II'>375</a>           |      | [Guess Number Higher or Lower   II](https://leetcode.com/problems/guess-number-higher-or-lower-ii) | 36.30%     | Medium     |      |
| 47   | <a href='#Wiggle Subsequence'>376</a>                        |      | [Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence) | 36.30%     | Medium     |      |
| 48   | <a href='#Combination Sum IV'>377</a>                        |      | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv) | 43.20%     | Medium     |      |
| 49   | <a href='#Is Subsequence'>392</a>                            |      | [Is Subsequence](https://leetcode.com/problems/is-subsequence) | 45.00%     | Medium     |      |
| 50   | <a href='#Burst Balloons'>312</a>                            |      | [Burst Balloons](https://leetcode.com/problems/burst-balloons) | 44.50%     | Hard       |      |
| 51   | <a href='#Frog Jump'>403</a>                                 |      | [Frog Jump](https://leetcode.com/problems/frog-jump)         | 33.50%     | Hard       |      |
| 52   | <a href='#Partition Equal Subset Sum'>416</a>                |      | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum) | 38.70%     | Medium     |      |
| 53   | <a href='#Sentence Screen Fitting'>418</a>                   |      | [Sentence Screen Fitting](https://leetcode.com/problems/sentence-screen-fitting) | 28.90%     | Medium     |      |
| 54   | <a href='#Split Array Largest Sum'>410</a>                   |      | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum) | 40.20%     | Hard       |      |
| 55   | <a href='#Wildcard Matching'>44</a>                          |      | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | 21.60%     | Hard       |      |
| 56   | <a href='#Arithmetic Slices'>413</a>                         |      | [Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices) | 54.50%     | Medium     |      |
| 57   | <a href='#Arithmetic Slices II -   Subsequence'>446</a>      |      | [Arithmetic Slices II -   Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence) | 28.00%     | Hard       |      |
| 58   | <a href='#Can I Win'>464</a>                                 |      | [Can I Win](https://leetcode.com/problems/can-i-win)         | 26.00%     | Medium     |      |
| 59   | <a href='#Unique Substrings in Wraparound   String'>467</a>  |      | [Unique Substrings in   Wraparound String](https://leetcode.com/problems/unique-substrings-in-wraparound-string) | 33.20%     | Medium     |      |
| 60   | <a href='#Count The Repetitions'>466</a>                     |      | [Count The Repetitions](https://leetcode.com/problems/count-the-repetitions) | 27.20%     | Hard       |      |
| 61   | <a href='#Encode String with Shortest   Length'>471</a>      |      | [Encode String with Shortest   Length](https://leetcode.com/problems/encode-string-with-shortest-length) | 43.70%     | Hard       |      |
| 62   | <a href='#Ones and Zeroes'>474</a>                           |      | [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes) | 38.70%     | Medium     |      |
| 63   | <a href='#Concatenated Words'>472</a>                        |      | [Concatenated Words](https://leetcode.com/problems/concatenated-words) | 32.00%     | Hard       |      |
| 64   | <a href='#Word Break'>139</a>                                |      | [Word Break](https://leetcode.com/problems/word-break)       | 32.60%     | Medium     |      |
| 65   | <a href='#Target Sum'>494</a>                                |      | [Target Sum](https://leetcode.com/problems/target-sum)       | 44.00%     | Medium     |      |
| 66   | <a href='#Predict the Winner'>486</a>                        |      | [Predict the Winner](https://leetcode.com/problems/predict-the-winner) | 45.60%     | Medium     |      |
| 67   | <a href='#Longest Palindromic Subsequence'>516</a>           |      | [Longest Palindromic   Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence) | 43.50%     | Medium     |      |
| 68   | <a href='#Super Washing Machines'>517</a>                    |      | [Super Washing Machines](https://leetcode.com/problems/super-washing-machines) | 36.30%     | Hard       |      |
| 69   | <a href='#Continuous Subarray Sum'>523</a>                   |      | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum) | 23.40%     | Medium     |      |
| 70   | <a href='#Remove Boxes'>546</a>                              |      | [Remove Boxes](https://leetcode.com/problems/remove-boxes)   | 36.90%     | Hard       |      |
| 71   | <a href='#Freedom Trail'>514</a>                             |      | [Freedom Trail](https://leetcode.com/problems/freedom-trail) | 39.60%     | Hard       |      |
| 72   | <a href='#Student Attendance Record II'>552</a>              |      | [Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii) | 31.60%     | Hard       |      |
| 73   | <a href='#Maximum Vacation Days'>568</a>                     |      | [Maximum Vacation Days](https://leetcode.com/problems/maximum-vacation-days) | 36.10%     | Hard       |      |
| 74   | <a href='#Out of Boundary Paths'>576</a>                     |      | [Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths) | 30.70%     | Medium     |      |
| 75   | <a href='#Non-negative   Integers without Consecutive Ones'>600</a> |      | [Non-negative Integers without   Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones) | 31.70%     | Hard       |      |
| 76   | <a href='#K Inverse Pairs Array'>629</a>                     |      | [K Inverse Pairs Array](https://leetcode.com/problems/k-inverse-pairs-array) | 27.90%     | Hard       |      |
| 77   | <a href='#Shopping Offers'>638</a>                           |      | [Shopping Offers](https://leetcode.com/problems/shopping-offers) | 46.20%     | Medium     |      |
| 78   | <a href='#Decode Ways II'>639</a>                            |      | [Decode Ways II](https://leetcode.com/problems/decode-ways-ii) | 24.20%     | Hard       |      |
| 79   | <a href='#Maximum Length of Pair Chain'>646</a>              |      | [Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain) | 47.30%     | Medium     |      |
| 80   | <a href='#Palindromic Substrings'>647</a>                    |      | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings) | 54.50%     | Medium     |      |
| 81   | <a href='#2 Keys Keyboard'>650</a>                           |      | [2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard) | 45.90%     | Medium     |      |
| 82   | <a href='#4 Keys Keyboard'>651</a>                           |      | [4 Keys Keyboard](https://leetcode.com/problems/4-keys-keyboard) | 49.80%     | Medium     |      |
| 83   | <a href='#Coin Path'>656</a>                                 |      | [Coin Path](https://leetcode.com/problems/coin-path)         | 25.80%     | Hard       |      |
| 84   | <a href='#Strange Printer'>664</a>                           |      | [Strange Printer](https://leetcode.com/problems/strange-printer) | 34.90%     | Hard       |      |
| 85   | <a href='#Number of   Longest Increasing Subsequence'>673</a> |      | [Number of Longest Increasing   Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence) | 32.00%     | Medium     |      |
| 86   | <a href='#Maximum Sum   of 3 Non-Overlapping Subarrays'>689</a> |      | [Maximum Sum of 3   Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays) | 42.00%     | Hard       |      |
| 87   | <a href='#Knight Probability in   Chessboard'>688</a>        |      | [Knight Probability in   Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard) | 40.80%     | Medium     |      |
| 88   | <a href='#Stickers to Spell Word'>691</a>                    |      | [Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word) | 36.00%     | Hard       |      |
| 89   | <a href='#Partition to K Equal Sum   Subsets'>698</a>        |      | [Partition to K Equal Sum   Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets) | 38.70%     | Medium     |      |
| 90   | <a href='#Minimum   ASCII Delete Sum for Two Strings'>712</a> |      | [Minimum ASCII Delete Sum for   Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings) | 52.00%     | Medium     |      |
| 91   | <a href='#Best Time to   Buy and Sell Stock with Transaction Fee'>714</a> |      | [Best Time to Buy and Sell   Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) | 47.70%     | Medium     |      |
| 92   | <a href='#Maximum Length of Repeated   Subarray'>718</a>     |      | [Maximum Length of Repeated   Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray) | 42.40%     | Medium     |      |
| 93   | <a href='#Minimum Window Subsequence'>727</a>                |      | [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence) | 32.80%     | Hard       |      |
| 94   | <a href='#Count   Different Palindromic Subsequences'>730</a> |      | [Count Different Palindromic   Subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences) | 36.50%     | Hard       |      |
| 95   | <a href='#Cherry Pickup'>741</a>                             |      | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup) | 24.80%     | Hard       |      |
| 96   | <a href='#Delete and Earn'>740</a>                           |      | [Delete and Earn](https://leetcode.com/problems/delete-and-earn) | 44.20%     | Medium     |      |
| 97   | <a href='#Min Cost Climbing Stairs'>746</a>                  |      | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs) | 44.00%     | Easy       |      |
| 98   | <a href='#Number Of Corner Rectangles'>750</a>               |      | [Number Of Corner Rectangles](https://leetcode.com/problems/number-of-corner-rectangles) | 59.00%     | Medium     |      |
| 99   | <a href='#Largest Plus Sign'>764</a>                         |      | [Largest Plus Sign](https://leetcode.com/problems/largest-plus-sign) | 41.30%     | Medium     |      |
| 100  | <a href='#Longest Palindromic Substring'>5</a>               |      | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) | 25.60%     | Medium     |      |
| 101  | <a href='#Domino and Tromino Tiling'>790</a>                 |      | [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling) | 33.70%     | Medium     |      |
| 102  | <a href='#Cheapest Flights Within K Stops'>787</a>           |      | [Cheapest Flights Within K   Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops) | 30.30%     | Medium     |      |
| 103  | <a href='#Minimum   Swaps To Make Sequences Increasing'>801</a> |      | [Minimum Swaps To Make   Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing) | 32.20%     | Medium     |      |
| 104  | <a href='#Soup Servings'>808</a>                             |      | [Soup Servings](https://leetcode.com/problems/soup-servings) | 34.30%     | Medium     |      |
| 105  | <a href='#Largest Sum of Averages'>813</a>                   |      | [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages) | 42.10%     | Medium     |      |
| 106  | <a href='#Race Car'>818</a>                                  |      | [Race Car](https://leetcode.com/problems/race-car)           | 29.60%     | Hard       |      |
| 107  | <a href='#New 21 Game'>837</a>                               |      | [New 21 Game](https://leetcode.com/problems/new-21-game)     | 26.00%     | Medium     |      |
| 108  | <a href='#Push Dominoes'>838</a>                             |      | [Push Dominoes](https://leetcode.com/problems/push-dominoes) | 41.40%     | Medium     |      |
| 109  | <a href='#Shortest Path Visiting All   Nodes'>847</a>        |      | [Shortest Path Visiting All   Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes) | 43.10%     | Hard       |      |
| 110  | <a href='#Minimum Number of Refueling   Stops'>871</a>       |      | [Minimum Number of Refueling   Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops) | 25.90%     | Hard       |      |
| 111  | <a href='#Length of   Longest Fibonacci Subsequence'>873</a> |      | [Length of Longest Fibonacci   Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence) | 41.90%     | Medium     |      |
| 112  | <a href='#Stone Game'>877</a>                                |      | [Stone Game](https://leetcode.com/problems/stone-game)       | 56.60%     | Medium     |      |
| 113  | <a href='#Profitable Schemes'>879</a>                        |      | [Profitable Schemes](https://leetcode.com/problems/profitable-schemes) | 31.90%     | Hard       |      |
| 114  | <a href='#Super Egg Drop'>887</a>                            |      | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop) | 22.20%     | Hard       |      |
| 115  | <a href='#Bitwise ORs of Subarrays'>898</a>                  |      | [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays) | 29.20%     | Medium     |      |
| 116  | <a href='#Numbers At Most N Given Digit   Set'>902</a>       |      | [Numbers At Most N Given Digit   Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set) | 25.10%     | Hard       |      |
| 117  | <a href='#Valid Permutations for DI   Sequence'>903</a>      |      | [Valid Permutations for DI   Sequence](https://leetcode.com/problems/valid-permutations-for-di-sequence) | 38.70%     | Hard       |      |

以下题目仅描述递归的解法：

##### Longest Valid Parentheses

"(()"-2

 ")()())"-4

额外使用一个数组d记录序列每一个位置当前的最大有效长度，以“()(())”为例



| 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | 2    | 0    | 0    | 2    | 4    |

从序列的第2个元素开始，直到遇到'')''记此时索引为c，这时会有两种情况：

- 当c-1是‘(’，那么可以确定这一组有效的，且如果从c>2的话，那么就是$d[c]=d[c-2]+2$，否则就是2
- 当c-1是‘)’，我们就需要排除掉c-1所对应的有效序列d[c-1]之前的那一位是不是'(',如果不是，就取0，如果是
  - 如果$c-d[c-1]-2 >0$,则$d[c] = d[c-1] + d[c-d[c-1]-2] + 2$
  - 否则$d[c] = d[c-1] + 2$

```python
class Solution(object):	
    def method3(self, s):
        """
        dp方法，是我想要能想到的方法
        创建数组记录每一个位置当前的最大有效长度
        """
        if not s:
            return 0
        d = [0] * len(s)
        ansmax = 0
        for c in range(1, len(s)):
            if s[c] == ')':
                if s[c-1] == '(':
                    d[c] = (d[c-2] if c > 2 else 0) + 2
                elif c - d[c-1] > 0 and s[c-d[c-1]-1] == '(':
                    d[c] = d[c-1] + ((d[c-d[c-1]-2]  if c-d[c-1]-2 > 0 else 0 ) + 2)
                ansmax=max(ansmax, d[c])
        return ansmax
```



##### Unique Paths II

和机器人收集硬币是一类问题，采用二维数据存储实时状态，将有障碍的位置初始为0，[c,h]的更新依赖于[c-1,h]和[c,h-1]的和

```python
class Solution(object):
    def method2(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        用例：[[1, 0]],[[0, 1]]
        """
        if not obstacleGrid:
            return 0
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        paths = [[0]*width for _ in range(height)]
        if obstacleGrid[0][0] != 1:
            paths[0][0] = 1
        
        for c in range(height):
            for h in range(width):
                if obstacleGrid[c][h] != 1:
                    if c > 0:
                        paths[c][h] += paths[c-1][h] 
                    if h > 0:
                        paths[c][h] += paths[c][h-1]
        return paths[-1][-1]
```



##### Minimum Path Sum

和机器人收集纪念币同样思路

```python
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        height = len(grid)
        width = len(grid[0])
        sums = [[0]*width for _ in range(height)]
        sums[0][0] = grid[0][0]
        for c in range(height):
            for h in range(width):
                if c > 0 and h > 0:
                    sums[c][h] = min(sums[c-1][h], sums[c][h-1]) + grid[c][h]
                elif c > 0:
                    sums[c][h] = sums[c-1][h] + grid[c][h]
                elif h > 0:
                    sums[c][h] = sums[c][h-1] + grid[c][h]
        return sums[-1][-1]
```



##### Edit Distance

我们定义3种操作，插入，删除和替换，对于将word1转化为word2，我一般习惯把word2放在列位置，记位置标记[c, h]，那么对于[c, h-1]执行的操作是添加，[c-1， h]执行的操作是删除，对于[c-1, h-1]，根据word1[c-1]和word2[h-1]是否相同添加相应的操作

```python
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.method1(word1, word2)
        
        
    def method1(self, word1, word2):
        """
        对于将word1转化为word2，我一般习惯把word2放在列位置，记位置标记[c, h]
        那么对于[c, h-1]执行的操作是添加，[c-1， h]执行的操作是删除，
        """
        width = len(word2) + 1
        height = len(word1) + 1
        margin = [[0]*width for _ in range(height)]
        for c in range(width):
            margin[0][c] = c
        for c in range(1, height):
            margin[c][0] = c
        # 按行遍历
        # for c in range(1, height):
        #     for h in range(1, width):
        #         indicator = 0 if word1[c-1] == word2[h-1] else 1
        #         margin[c][h] = min(margin[c-1][h] + 1,  # deletion
        #                            margin[c][h-1] + 1,  # insertion
        #                            margin[c-1][h-1] + indicator)
        # 按列遍历
        for c in range(1, width):
            for h in range(1, height):
                indicator = 0 if word1[h-1] == word2[c-1] else 1
                margin[h][c] = min(margin[h-1][c]+1,
                                  margin[h][c-1]+1,
                                  margin[h-1][c-1]+indicator)
        return margin[-1][-1]
```

以将Sartuday 转化为Sunday为例(按列遍历,这样对于任意的列字符，都可以自底向前追溯操作过程，更好理解)：

|      |      | S     | u     | n     | d     | a     | y     |
| ---- | ---- | ----- | ----- | ----- | ----- | ----- | ----- |
|      | 0    | 1     | 2     | 3     | 4     | 5     | 6     |
| S    | 1    | **0** | 1     | 2     | 3     | 4     | 5     |
| a    | 2    | **1** | 1     | 2     | 3     | 4     | 5     |
| t    | 3    | **2** | 2     | 2     | 3     | 4     | 5     |
| u    | 4    | 3     | **2** | 3     | 3     | 4     | 5     |
| r    | 5    | 4     | 3     | **3** | 4     | 4     | 5     |
| d    | 6    | 5     | 4     | 4     | **3** | 4     | 5     |
| a    | 7    | 6     | 5     | 5     | 4     | **3** | 4     |
| y    | 8    | 7     | 6     | 6     | 5     | 4     | **3** |
|      |      |       |       |       |       |       |       |



##### Scramble String

对于方法一，动态规划的自顶向下递归方法，分为两类情况：

- 从前向后将s1和s2分别切成两段，分别比较这两段是否是Scramble String
- s1从后向前分割，s2仍从前往后分割，分别比较这两段是否是Scramble String

对于方法二，动态规划的自底向上的循环实现，递推关系如下：

dp\[l\]\[c\]\[h\] = (dp\[y\]\[c\]\[h\] and dp\[l-y\]\[c+y\][h+y]) or (dp\[y\]\[c+l-y\][h] and dp\[l-y\]\[c\][h+y])

dp\[l\]\[c\]\[h\]表示s1和s2分别从c和h开始的长度为l的子串是否是Scramble String

```python
class Solution:
    def __init__(self):
        self.mem = {}
    
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return self.method2(s1, s2)
    
    def method1(self, s1, s2):
        """
        动态规划的recursive + cache模式
        没有sorted(s1) != sorted(s2)判断超时
        192 / 283 test cases passed.
        "abcdefghijklmn"
        "efghijklmncadb"
        """
        if not s1 or not s2:
            return False
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.mem[(s1, s2)] = False
            return False
        if s1 == s2:
            self.mem[(s1, s2)] = True
            return True
        if (s1, s2) in self.mem:
            return self.mem[(s1, s2)]
        ret = False
        for c in range(1, len(s1)):
            if (self.method1(s1[:c], s2[:c]) and self.method1(s1[c:], s2[c:])) or  (self.method1(s1[:c], s2[-c:]) and self.method1(s1[c:], s2[:-c])):
                ret = True
                self.mem[(s1, s2)] = ret
                return True
        self.mem[(s1, s2)] = ret
        return False
    
    def method2(self, s1, s2):
        if not s1 or not s2:
            return False
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        size = len(s1)
        dp = [ [[False]*size for _ in range(size)] for _ in range(size+1)]
        for c in range(size):
            for h in range(size):
                dp[1][c][h] = (s1[c] ==s2[h])
        for l in range(2, size+1):
            for c in range(size-l+1):
                for h in range(size-l+1):
                    for y in range (1, l):
                        if not dp[l][c][h]:
                            dp[l][c][h] = (dp[y][c][h] and dp[l-y][c+y][h+y]) or (dp[y][c+l-y][h] and dp[l-y][c][h+y])
        return dp[size][0][0]

```



##### Unique Binary Search Trees II

与树有关的问题很明确是动态规划问题，左右子树的处理和整个序列的处理是一样的，唯一需要注意的是对于每一个跟节点，需要分别求出左右子树可能的集合再做拼接

另外也需要注意基本案例，即start>end和start==end的情况

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n ==0:
            return []
        return self.method1(1, n)
    
    def method1(self, start, end):
        if start > end:
            return [None]
        if start == end:
            root = TreeNode(end)
            return [root]
        ret = []
        for c in range(start, end+1):
           
            left = self.method1(start, c-1)
            right = self.method1(c+1, end)
            
            for node1 in left:
                for node2 in right:
                    root = TreeNode(c)
                    root.left = node1
                    root.right = node2
                    ret.append(root)
        return ret

```



##### Interleaving String

和机器人收集硬币及编辑距离是一类问题，二阶动态规划

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self.method2(s1, s2, s3)
    
    def method2(self, s1, s2, s3):
        if not s1 and not s2 and not s3:
            return True
        if len(s3) != len(s1) + len(s2):
            return False
        
        height = len(s1) + 1
        width = len(s2) + 1
        
        dp = [[False]*width for _ in range(height)]
        
        for c in range(height):
            for h in range(width):
                if c == 0 and h == 0:
                    dp[c][h] = True
                elif c == 0 and h > 0:
                    dp[c][h] = dp[c][h-1] and s2[h-1] == s3[c+h-1]
                elif h == 0 and c > 0:
                    dp[c][h] = dp[c-1][h] and s1[c-1] == s3[c+h-1]
                else:
                    dp[c][h] = dp[c-1][h] and s1[c-1] == s3[c+h-1] or dp[c][h-1] and s2[h-1] == s3[c+h-1]
        return dp[-1][-1]
```



##### Distinct Subsequences

s->t

额外使用一个数组记录t中每一个字符出现的次数，数组初始化为0

匹配的规则是：对于s中的每一个字符，从后向前对t进行匹配，匹配的递推关系为：

$prefix[c]=prefix[c] + (prefix[c-1] if c>0 else 1)$

```python
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return self.method1(s, t)
    
    def method1(self, s, t):
        if not s or not t:
            return 0
        if s == t:
            return 1
        
        prefix = [0]*len(t)
        for item in s:
            for c in range(len(t))[::-1]:
                if item == t[c]:
                    prefix[c] = prefix[c] + (prefix[c-1] if c > 0 else 1)
        return prefix[-1]
```

| b    | a    | g     |      |
| ---- | ---- | ----- | ---- |
| 0    | 0    | 0     |      |
| 1    | 0    | 0     | b    |
| 1    | 1    | 0     | a    |
| 2    | 1    | 0     | b    |
| 2    | 1    | 1     | g    |
| 3    | 1    | 1     | b    |
| 3    | 4    | 1     | a    |
| 3    | 4    | **5** | g    |

输出5

##### Triangle

dfs，对层数进行递归，并需要根据当前层元素的index索引限制下层元素的索引index和index+1

递归表达式

$ total = min(total, curr + self.minimum_total(triangle, level+1, c))$

c是当前层元素索引

```python
import sys
class Solution:
    
    def __init__(self):
        self.mem = {}
        
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return self.minimum_total(triangle, 0, 0)
        
    def minimum_total(self, triangle, level, index):
        """
        未加缓存会在42/43超时
        """
        if level > len(triangle)-1:
            return 0
        if (level, index) not in self.mem:
            total = sys.maxsize
            for c, item in enumerate(triangle[level]):
                if c >= index and c < index + 2:
                    curr = item
                    total = min(total, curr + self.minimum_total(triangle, level+1, c))
            self.mem[(level, index)] = total
        return self.mem[(level, index)]

```



##### Best Time to Buy and Sell Stock II

采用动态规划dp(i,j)表示i次操作在第j天的最大收益

dp(i,j) = max(dp(i, j-1), max[dp(i-1, k) + prices[i]-pricesp[k] for k from 0 to i]),dp(0, j)=0, dp(i,0)=0

```python
def max_profit(prices):
    if not prices:
        return 0
    k = 2
    dp = [[0]* len(prices) for _ in range(k+1)]
    ret = 0
    for i in range(1, k+1):
        temp_max = dp[i][0] - prices[0]
        for j in range(1, len(prices)):
            dp[i][j] = max(dp[i][j-1], temp_max + prices[j])
            temp_max = max(dp[i-1][j] - prices[j], temp_max)
            ret = max(ret, dp[i][j])
    return ret
```

上面的结果在k=2时有很多重复计算，因而可以先计算一次操作的每天最大收益，然后从后往前推两次操作可以达到的最大收益

```python
def max_profit(prices):
    if not prices:
        return 0
    curr_min = prices[0]
    max_profits = 0
    profits = []
    for price in prices:
        curr_min = min(curr_min, price)
        max_profits = max(max_profits, price - curr_min)
        profits.append(max_profits)
        
    total = 0
    curr_max = prices[-1]
    max_profits = 0
    for i in range(len(prices)-1, -1, -1):
        curr_max = max(curr_max, prices[i])
        max_profits = max(max_profits, curr_max-prices[i])
        total = max(total, profits[i] + max_profits)
    return total  
```



##### Palindrome Partitioning II

##### Maximum Product Subarray

##### Best Time to Buy and Sell Stock IV

##### House Robber

##### House Robber II

##### Paint House

##### Ugly Number II

##### Paint House II

##### Paint Fence

##### Perfect Squares

##### Longest Increasing Subsequence

##### Range Sum Query - Immutable

##### Range Sum Query 2D - Immutable

##### Best Time to Buy and Sell Stock with Cooldown

##### Create Maximum Number

##### Coin Change

##### Counting Bits

##### Integer Break

##### Maximal Rectangle

##### Maximal Square

##### Best Time to Buy and Sell Stock

##### Dungeon Game

##### Unique Binary Search Trees

##### Decode Ways

##### Regular Expression Matching

##### Unique Paths

##### Maximum Subarray

##### Climbing Stairs

##### Word Break II

##### Russian Doll Envelopes

##### Android Unlock Patterns

##### Count Numbers with Unique Digits

##### Bomb Enemy

##### Max Sum of Rectangle No Larger Than K

##### Largest Divisible Subset

##### Guess Number Higher or Lower II

##### Wiggle Subsequence

##### Combination Sum IV

##### Is Subsequence

##### Burst Balloons

##### Frog Jump

##### Partition Equal Subset Sum

##### Sentence Screen Fitting

##### Split Array Largest Sum

##### Wildcard Matching

##### Arithmetic Slices

##### Arithmetic Slices II - Subsequence

##### Can I Win

##### Unique Substrings in Wraparound String

##### Count The Repetitions

##### Encode String with Shortest Length

##### Ones and Zeroes

##### Concatenated Words

##### Word Break

##### Target Sum

##### Predict the Winner

##### Longest Palindromic Subsequence

##### Super Washing Machines

##### Continuous Subarray Sum

##### Remove Boxes

##### Freedom Trail

##### Student Attendance Record II

##### Maximum Vacation Days

##### Out of Boundary Paths

##### Non-negative Integers without Consecutive Ones

##### K Inverse Pairs Array

##### Shopping Offers

对于每一次给定的条件，需要先计算不用优惠的价格，以及使用不同优惠券的价格，在每次使用完优惠券之后，得到新的needs,将当前优惠的价格和新needs需要的价格相加得到用券后的价格，与原始价格比较取较小值

递推关系如下：
$$
cost = min(cost, s[-1] + self.method1(price, special, needs))
$$
同时不妨加入缓存

```python
class Solution:
    
    def __init__(self):
        self.mem = {}
        
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.method1(price, special, needs)
    
    def cost_sum(self, price, needs):
        cost = 0
        for c, need in enumerate(needs):
            cost += need * price[c]
        return cost
        
    
    def method1(self, price, special, needs):
        """
        未加缓存Runtime: 128 ms
        之后Runtime: 76 ms，40%非常客观的提升
        
        """
        if tuple(needs) in self.mem:
            return self.mem[tuple(needs)]
        if not price or not special or not needs:
            return 0
        cost = self.cost_sum(price, needs)
        for s in special:
            clone = needs[:]
            c = 0
            while c < len(clone):       
                if s[c] > clone[c]:
                    break
                clone[c] -= s[c]
                c += 1
            if c == len(clone):
                cost = min(cost, s[-1] + self.method1(price, special, clone))
        self.mem[tuple(needs)] = cost
        return self.mem[tuple(needs)]

```



##### Decode Ways II

##### Maximum Length of Pair Chain

##### Palindromic Substrings

##### 2 Keys Keyboard

##### 4 Keys Keyboard

##### Coin Path

##### Strange Printer

##### Number of Longest Increasing Subsequence

##### Maximum Sum of 3 Non-Overlapping Subarrays

##### Knight Probability in Chessboard

##### Stickers to Spell Word

##### Partition to K Equal Sum Subsets

##### Minimum ASCII Delete Sum for Two Strings

##### Best Time to Buy and Sell Stock with Transaction Fee

##### Maximum Length of Repeated Subarray

##### Minimum Window Subsequence

##### Count Different Palindromic Subsequences

##### Cherry Pickup

##### Delete and Earn

##### Min Cost Climbing Stairs

##### Number Of Corner Rectangles

##### Largest Plus Sign

##### Longest Palindromic Substring

##### Domino and Tromino Tiling

##### Cheapest Flights Within K Stops

##### Minimum Swaps To Make Sequences Increasing

##### Soup Servings

##### Largest Sum of Averages

##### Race Car

##### New 21 Game

##### Push Dominoes

##### Shortest Path Visiting All Nodes

##### Minimum Number of Refueling Stops

##### Length of Longest Fibonacci Subsequence

##### Stone Game

##### Profitable Schemes

##### Super Egg Drop

##### Bitwise ORs of Subarrays

##### Numbers At Most N Given Digit Set

##### Valid Permutations for DI Sequence

**参考**

[Dynamic Programming: First Principles](http://www.flawlessrhetoric.com/Dynamic-Programming-First-Principles)

[利润最大化](https://lukasmericle.github.io/dynprotut/)



