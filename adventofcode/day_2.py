def calcChecksum(doubleList, differenceOrDivision):
    if(differenceOrDivision):
        lineResults = calcDifferences(doubleList)
    else:
        lineResults = calcEvenDivisions(doubleList)
    return sum(lineResults)


def calcDifferences(doubleList):
    differenceList = list()
    for row in doubleList:
        lowest = row[0]
        biggest = row[0]
        for i in range(len(row)):
            if row[i] > biggest:
                biggest = row[i]
            elif row[i] < lowest:
                lowest = row[i]
        differenceList.append(biggest - lowest)
    return differenceList


def calcEvenDivisions(doubleList):
    divisonsList = list()
    for row in doubleList:
        for i in range(len(row)):
            divisionChecker = row[i]
            for j in range(i + 1, len(row)):
                division = 0.0
                if divisionChecker > row[j]:
                    division = divisionChecker / row[j]
                elif divisionChecker < row[j]:
                    division = row[j] / divisionChecker

                if division.is_integer():
                    divisonsList.append(int(division))
                    break
    return divisonsList


def doubleListOfStrings(randomString):
    listOfStrings = randomString.split("\n")
    doubleList = list()
    for s in listOfStrings:
        intList = list(map(int, s.split("\t")))
        doubleList.append(intList)
    return doubleList


inputList = """116	1259	1045	679	1334	157	277	1217	218	641	1089	136	247	1195	239	834
269	1751	732	3016	260	6440	5773	4677	306	230	6928	7182	231	2942	2738	3617
644	128	89	361	530	97	35	604	535	297	599	121	567	106	114	480
105	408	120	363	430	102	137	283	123	258	19	101	181	477	463	279
873	116	840	105	285	238	540	22	117	125	699	953	920	106	113	259
3695	161	186	2188	3611	2802	157	2154	3394	145	2725	1327	3741	2493	3607	4041
140	1401	110	119	112	1586	125	937	1469	1015	879	1798	122	1151	100	926
2401	191	219	607	267	2362	932	2283	889	2567	2171	2409	1078	2247	2441	245
928	1142	957	1155	922	1039	452	285	467	305	506	221	281	59	667	232
3882	1698	170	5796	2557	173	1228	4630	174	3508	5629	4395	180	5100	2814	2247
396	311	223	227	340	313	355	469	229	162	107	76	363	132	453	161
627	1331	1143	1572	966	388	198	2068	201	239	176	1805	1506	1890	1980	1887
3390	5336	1730	4072	5342	216	3823	85	5408	5774	247	5308	232	256	5214	787
176	1694	1787	1586	3798	4243	157	4224	3603	2121	3733	851	2493	4136	148	153
2432	4030	3397	4032	3952	2727	157	3284	3450	3229	4169	3471	4255	155	127	186
919	615	335	816	138	97	881	790	855	89	451	789	423	108	95	116"""

print(calcChecksum(doubleListOfStrings(inputList), True))
print(calcChecksum(doubleListOfStrings(inputList), False))
