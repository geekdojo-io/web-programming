### Quiz - Week 7

Q1 - What is the final value for x and y?

```python
x = 3
y = 4
x *= y * x + 1
```

<details><summary>Solution</summary>
<p>

##### Answer
x = 39
y = 4 

##### Explanation
x = 3 * (4 * 3 + 1), y is unchanged.

</p>
</details>

---

Q2 - What is the output for `Theano[-3]`?

    A - 'e'
    B - 'a'
    C - 'n'
    D - 'o'

<details><summary>Solution</summary>
<p>

##### Anwer
B

##### Explanation
Negative indexes begin toward the end of a string and go in reverse.

</p>
</details>

---


Q3 - What is output of the following code?

```python
print('Corgie'.split('o'))
```

    A - ('Corgie', '')
    B - ('Corgie', 'Co', 'orgie')
    C - ('C', 'orgie')
    D - ('C', 'rgie')

<details><summary>Solution</summary>
<p>

##### Anwer
D

##### Explanation
The `split()` method splits a string into a list. You can specify the separator, and in the question, the separate was `'o'`. 'Corgie' separated by 'o' is ('C', 'rgie').

</p>
</details>


Q4 - What is output of following code?

```python
def foo(x, ans):
    if (x == 0):
        return ans
    else:
        return foo(x - 1, x + ans)

print(foo(2, 0))
```

<details><summary>Solution</summary>
<p>

##### Anwer
3

##### Explanation
The code is using recursion. Recursion is a a method that calls itself.

- First call: foo(2, 0) # The first call was triggered by `print(foo(2, 0))`.
- Second call: foo(1, 2) # This is because 1 = 2 - 1, and 2 = 2 + 0
- Third call: foo(0, 3) # Now, because x = 0, the code will return `ans` which is 3.

</p>
</details>

Q5 - What is output of following code?

```python
arr = [1, 2, 4, 8, 7]
arr.insert(2, 15)

```


<details><summary>Solution</summary>
<p>

##### Anwer
[1, 2, 15, 4, 8, 7]

##### Explanation
`list.insert(index, element)` method is used to insert a item at certain position in a list. `index` defines position at which the `element` will be added. 

</p>
</details>