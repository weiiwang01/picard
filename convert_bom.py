import csv
import pathlib
import sys

production = pathlib.Path(sys.argv[1])

positions = csv.reader((production / "positions.csv").open())
connectors = []

for row in positions:
    reference, x, y, rotation, layer = row
    if not reference.startswith("ComputeModule"):
        continue
    x = float(x)
    y = float(y)
    connectors.append((f"X{len(connectors)+1}", x + 21.5, y + 0.46, rotation, layer)) 
    connectors.append((f"X{len(connectors)+1}", x + 21.5, y - 33.46, rotation, layer))

(production / "positions.csv").open(mode="a").write(
    "\n".join(",".join(map(str, c)) for c in connectors) + "\n"
)
(production / "bom.csv").open(mode="a").write(
    '"{}",DF40C-100DS-0.4v,{},DF40C-100DS-0.4v,'.format(
        ", ".join(r[0] for r in connectors), len(connectors)
    )
)
