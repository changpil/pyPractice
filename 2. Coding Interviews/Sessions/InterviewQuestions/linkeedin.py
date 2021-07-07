"""
change ROMAN numbers to integer
I, II, III, IV, V, VI, VIII, IX X

Pattern1:knapsack	I	Pattern1:knapsack
2	II	Pattern1:knapsack+Pattern1:knapsack
3	III	Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
4	IV	5-Pattern1:knapsack
5	V	5
6	VI	5+Pattern1:knapsack
7	VII	5+Pattern1:knapsack+Pattern1:knapsack
8	VIII	5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
9	IX	10-Pattern1:knapsack
10	X	10
11	XI	10+Pattern1:knapsack
12	XII	10+Pattern1:knapsack+Pattern1:knapsack
13	XIII	10+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
14	XIV	10-Pattern1:knapsack+5
15	XV	10+5
16	XVI	10+5+Pattern1:knapsack
17	XVII	10+5+Pattern1:knapsack+Pattern1:knapsack
18	XVIII	10+5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
19	XIX	10-Pattern1:knapsack+10
20	XX	10+10
21	XXI	10+10+Pattern1:knapsack
22	XXII	10+10+Pattern1:knapsack+Pattern1:knapsack
23	XXIII	10+10+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
24	XXIV	10+10-Pattern1:knapsack+5
25	XXV	10+10+5
26	XXVI	10+10+5+Pattern1:knapsack
27	XXVII	10+10+5+Pattern1:knapsack+Pattern1:knapsack
28	XXVIII	10+10+5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
29	XXIX	10+10-Pattern1:knapsack+10
30	XXX	10+10+10
31	XXXI	10+10+10+Pattern1:knapsack
32	XXXII	10+10+10+Pattern1:knapsack+Pattern1:knapsack
33	XXXIII	10+10+10+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
34	XXXIV	10+10+10-Pattern1:knapsack+5
35	XXXV	10+10+10+5
36	XXXVI	10+10+10+5+Pattern1:knapsack
37	XXXVII	10+10+10+5+Pattern1:knapsack+Pattern1:knapsack
38	XXXVIII	10+10+10+5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
39	XXXIX	10+10+10-Pattern1:knapsack+10
40	XL	50-10
41	XLI	50-10+Pattern1:knapsack
42	XLII	50-10+Pattern1:knapsack+Pattern1:knapsack
43	XLIII	50-10+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
44	XLIV	50-10-Pattern1:knapsack+5
45	XLV	50-10+5
46	XLVI	50-10+5+Pattern1:knapsack
47	XLVII	50-10+5+5+Pattern1:knapsack
48	XLVIII	50-10+5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
49	XLIX	50-10-Pattern1:knapsack+10
50	L	50
51	LI	50+Pattern1:knapsack
52	LII	50+Pattern1:knapsack+Pattern1:knapsack
53	LIII	50+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
54	LIV	50-Pattern1:knapsack+5
55	LV	50+5
56	LVI	50+5+Pattern1:knapsack
57	LVII	50+5+Pattern1:knapsack+Pattern1:knapsack
58	LVIII	50+5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
59	LIX	50-Pattern1:knapsack+10
60	LX	50+10
61	LXI	50+10+Pattern1:knapsack
62	LXII	50+10+Pattern1:knapsack+Pattern1:knapsack
63	LXIII	50+10+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
64	LXIV	50+10-Pattern1:knapsack+5
65	LXV	50+10+5
66	LXVI	50+10+5+Pattern1:knapsack
67	LXVII	50+10+5+Pattern1:knapsack+Pattern1:knapsack
68	LXVIII	50+10+5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
69	LXIX	50+10-Pattern1:knapsack+10
70	LXX	50+10+10
71	LXXI	50+10+10+Pattern1:knapsack
72	LXXII	50+10+10+Pattern1:knapsack+Pattern1:knapsack
73	LXXIII	50+10+10+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
74	LXXIV	50+10+10-Pattern1:knapsack+5
75	LXXV	50+10+10+5
76	LXXVI	50+10+10+5+Pattern1:knapsack
77	LXXVII	50+10+10+5+Pattern1:knapsack+Pattern1:knapsack
78	LXXVIII	50+10+10+5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
79	LXXIX	50+10+10-Pattern1:knapsack+10
80	LXXX	50+10+10+10
81	LXXXI	50+10+10+10+Pattern1:knapsack
82	LXXXII	50+10+10+10+Pattern1:knapsack+Pattern1:knapsack
83	LXXXIII	50+10+10+10+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
84	LXXXIV	50+10+10+10-Pattern1:knapsack+5
85	LXXXV	50+10+10+10+5
86	LXXXVI	50+10+10+10+5+Pattern1:knapsack
87	LXXXVII	50+10+10+10+5+Pattern1:knapsack+Pattern1:knapsack
88	LXXXVIII	50+10+10+10+5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
89	LXXXIX	50+10+10+10-Pattern1:knapsack+10
90	XC	100-10
91	XCI	100-10+Pattern1:knapsack
92	XCII	100-10+Pattern1:knapsack+Pattern1:knapsack
93	XCIII	100-10+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
94	XCIV	100-10-Pattern1:knapsack+5
95	XCV	100-10+5
96	XCVI	100-10+5+Pattern1:knapsack
97	XCVII	100-10+5+Pattern1:knapsack+Pattern1:knapsack
98	XCVIII	100-10+5+Pattern1:knapsack+Pattern1:knapsack+Pattern1:knapsack
99	XCIX	100-10-Pattern1:knapsack+10
100	C	100
200	CC	100+100
300	CCC	100+100+100
400	CD	500-100
500	D	500
600	DC	500+100
700	DCC	500+100+100
800	DCCC	500+100+100+100
900	CM	1000-100
1000	M	1000
5000	V
10000	X
50000	L
100000	C
500000	D
1000000	M

"""

RomanToInteger ={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def romanToInteger(roman):
    inte = 0
    prev=RomanToInteger[roman[0]]
    for i in roman[1:]:
        c = RomanToInteger[i]
        if prev >= c:
            inte += prev
        else:
            inte -= prev
        prev=c
    return inte + RomanToInteger[roman[-1]]





print(str(romanToInteger("LXXXVI")))