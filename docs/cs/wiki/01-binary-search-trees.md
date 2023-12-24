Binary Search Trees
===

Traversal
---

### Inorder Traversal

[Video](https://www.youtube.com/watch?v=5dySuyZf9Qg)

**Procedure:**

- Traverse Left subtree
- Visit node
- Traverse Right subtree

```java
public static void inOrder(Node root) {
        if (root == null){
            return;
        }
        inOrder(root.left);
        System.out.print(root.data + " ");
        inOrder(root.right);
    }
```

### Preorder Traversal

[Video](https://www.youtube.com/watch?v=1WxLM2hwL-U)

**Procedure:**

- Visit node
- Traverse Left subtree
- Traverse Right subtree

### Postorder Traversal

[Video](https://www.youtube.com/watch?v=4zVdfkpcT6U)

**Procedure:**

- Traverse Left subtree
- Traverse Right subtree
- Visit node
