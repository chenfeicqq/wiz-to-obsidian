import os.path
from pathlib import Path

a = Path("/My Notes/学习/技术领域/前端/可视化/ECharts.md")

b = Path("/My Notes/学习/技术领域/前端/abc/ECharts1.md")

# print(a.relative_to(b))

path = os.path.relpath(str(b), os.path.dirname(str(a)))

print(path)
