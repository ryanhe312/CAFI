print("This script automatically convert TrakeMate track to ISBI format and evaluate the metrics. ")
print()

while True:
    print("Please drag files to the command window to input paths.")
    print()
    reference = input("Reference Track: ").strip('"')
    candidate = input("Candidate Track: ").strip('"')

    print("Converting ISBI format...")
    print()
    with open(reference, 'r') as f:
        lines_r = f.readlines()
    with open(candidate, 'r') as f:
        lines_c = f.readlines()
    lines = lines_r[:3] + lines_c[2:-1] + lines_r[-2:]
    convert = candidate[:-4]+"_ISBI.xml"
    with open(convert, 'w') as f:
        f.writelines(lines)

    print("Evaluating ISBI performance...")
    import subprocess
    p = subprocess.Popen(["java", "-jar", "trackingPerformanceEvaluation.jar", "-r", reference, "-c", convert], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = []
    for line in p.stdout.readlines():
        lines.append(line.decode())
        print(line.decode())
    retval = p.wait()
    result = candidate[:-4]+"_ISBI.txt"
    with open(result, 'w') as f:
        f.writelines(lines)
    input("Please press Any key to continue...")
