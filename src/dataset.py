import pandas as pd

# 2. creating data frame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 37, 22, 32],
    "City": ["New york", "Los Angeles", "Chicag", "Houston"],
}
df = pd.DataFrame(data)

df.head(3)
df.replace("Alice", "Alice Smith")
