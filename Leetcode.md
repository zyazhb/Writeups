# [相关链接](https://onedrive.live.com/view.aspx?resid=66FB1CA2D2605783%21664&id=documents&wd=target%28%E5%AD%A6%E4%B9%A0%E5%8C%BA%E5%9F%9F.one%7CCEBA8BBB-5A0A-E240-9F81-CDFE4F659533%2F%E5%81%87%E8%A3%85%E5%9C%A8%E5%AD%A6leetcode%7C4DCBAEC4-2016-4144-8612-6107098E047F%2F%29onenote:https://d.docs.live.net/66fb1ca2d2605783/文档/Family%20Notebook/学习区域.one#假装在学leetcode&section-id={CEBA8BBB-5A0A-E240-9F81-CDFE4F659533}&page-id={4DCBAEC4-2016-4144-8612-6107098E047F}&object-id={CD2C297F-74D0-4BD9-8408-0204D0DD698C}&57)
[Leetcode Problemset](https://leetcode.com/problemset/all/)  
[Python Answer](https://github.com/librauee/leetcode)
# 总结
## 1. Two Sum
map和unordered_map的差别和使用  
enumerate() 函数用于将一个可遍历的数据对象。
```python 
#44ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {} #字典
        for i , num in enumerate(nums):
            complement = target - num
            if complement in record:
                return [record[complement],i]
            else:
                record[num] = i
```
使用if else比两个if节省时间
## 7. Reverse Integer
```python
	#32ms
	class Solution:
	    def reverse(self, x: int) -> int:
	        if x > 0 :
	            solution = int(str(x)[::-1])
	        else :
	            solution = -1 * int(str(x*-1)[::-1])
		#处理溢出的情况
	        min = -2**31
	        max = 2**31 -1
	        if solution in range(min,max):
	            return solution
	        else:
	            return 0
```
## 9. Palindrome Number 
python的回文果然为所欲为
    
```python
    #44ms
	class Solution:
	    def isPalindrome(self, x: int) -> bool:
	        return str(x) == str(x)[::-1]
```
## 13. Roman to Integer  
罗马数字的精髓
```python
	class Solution:
	    def romanToInt(self, s: str) -> int:
	        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	        result = 0
	        for i in range(len(s)-1):
	            if(dic[s[i]]<dic[s[i+1]]):
	                result-=dic[s[i]]
	            else:
	                result+=dic[s[i]]
	        result+=dic[s[len(s)-1]]
	        return result
```
## 14. Longest Common Prefix  
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:	#["flower","flow","flight"]
        if not strs: return ""					#无输入返回空值
        if len(strs) == 1: return strs[0]			#只有一个值返回该值
        strs.sort()						#先排序['flight', 'flow', 'flower']
        p=""							#初始化最长公共串
        for x,y in zip(strs[0],strs[-1]):			#[('f', 'f'), ('l', 'l'), ('i', 'o'), ('g', 'w'), ('h', 'e'), ('t', 'r')]
            if x == y :
                p+=x
            else:
                break
        return p						#fl
```
## 20. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses)    
一个简单但是效率不高的写法
```python
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()","").replace("[]","").replace("{}","")
        return s == ''
```
使用了堆栈但是速度还有提升空间
```python
    map = {"(": ")", "[": "]",  "{": "}"}
    stack = []
    for i in s:
        if i in map:
            stack.append(i)
        elif stack and i == map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []
```
## 21. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            res = l1
            l1 = l1.next
        else:
            res = l2
            l2 = l2.next
        temp = res
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1 != None:
            temp.next = l1
        else:
            temp.next = l2
        return res 
```
## []()
```python
```
