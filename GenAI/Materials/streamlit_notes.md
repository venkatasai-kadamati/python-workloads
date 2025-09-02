### Dropdown selection

> Use a selectbox method

```python
# template
style_input = st.selectbox(
        "Select [description]",
        [list of options],
)

# example
style_input = st.selectbox(
        "Select Explanation Style",
        ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)
```

### Heading

> Use a header method

```python
st.header("Page Header")
```