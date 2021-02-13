# arithmetic-formatter
Simple arithmetic formatter with Python 3.7 

Challenge project made for Scientific Computing with Python Certification at freeCodeCamp. The prompt was: "Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed."

So the functin output for:

arithmetic_arranger(["32 + 8", "1 - 3801", "45 + 43", "523 - 49"], True)

Will be:

  32         1        45      523
+  8    - 3801    +   43    -  49
----    ------    ------    -----
  40     -3800        88      474

