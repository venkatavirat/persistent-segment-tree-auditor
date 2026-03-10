# Persistent Segment Tree for audit trails - IITH SURE 2026
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2*node+1, start, mid)
        self.build(arr, 2*node+2, mid+1, end)
        self.tree[node] = min(self.tree[2*node+1], self.tree[2*node+2])
    
    def query(self, node, start, end, l, r):
        if r < start or end < l: return float('inf')
        if l <= start and end <= r: return self.tree[node]
        mid = (start + end) // 2
        left = self.query(2*node+1, start, mid, l, r)
        right = self.query(2*node+2, mid+1, end, l, r)
        return min(left, right)

# Demo
data = [3,1,4,1,5,9,2,6]
st = SegmentTree(data)
print("Min [1-4]:", st.query(0, 0, 7, 1, 4))  # Output: 1
