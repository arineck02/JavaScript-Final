import csv

def read_golfers():
    golfers = []
    with open("golfers.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            
            par_strokes_str = row["par_strokes"].strip("[]")
            par_strokes = []
            if par_strokes_str:
                for item in par_strokes_str.split("),"):
                    item = item.strip("()")
                    par, strokes = map(int, item.split(","))
                    par_strokes.append((par, strokes))
            row["par_strokes"] = par_strokes
            
            
            score_dif_str = row["score_dif"].strip("[]") 
            score_dif = list(map(int, score_dif_str.split(","))) if score_dif_str else []
            row["score_dif"] = score_dif
            
            row["total_score"] = int(row["total_score"]) 
            golfers.append(row)
    
    return golfers

def write_golfers(golfers):
    with open("golfers.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "full_name", "par_strokes", "score_dif", "total_score"])
        for golfer in golfers:
            par_strokes_str = str(golfer["par_strokes"]).replace("),", "), ")
            score_dif_str = str(golfer["score_dif"])  
            
            writer.writerow([
                golfer["id"],
                golfer["full_name"],
                par_strokes_str,
                score_dif_str,
                golfer["total_score"]
            ])
