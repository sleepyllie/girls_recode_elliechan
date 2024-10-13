# function for hyperlinks.
def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)

# color changers, and fonts
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   # if Q break

# welcome statements
print("\n" + color.BOLD + '\t' + 'Welcome to the high school FREE educational links portal!' + '\t\n' + color.END)
print("Below, categories of educational website links are sorted by their categories/sections. \nTo access, please input one of the numbers when instructed to do so.\n")

while True:
    choice = input(color.CYAN + "\nPlease enter one of the following categories by their number, or enter Q to quit at any time:" + color.END + " \n1. Math (Algebras, Geometry, etc.).\n2. English Language Arts (ELA).\n3. Sciences (Including Computer Sciences).\n4. Histories (World, US), Economics, & Art.\n5. Standardized Testing Prep.\nEnter choice here: ")
    if choice == "Q":
        break
    if choice == "1":
        choice1 = input("\nYou have selected: Math (Algebras, Geometry, etc.)\n1. Algebra 1.\n2. Geometry.\n3. Algebra 2.\n4. Precalculus.\n5. AP Calculus AB.\n6. AP Calculus BC.\n7. Statistics.\nEnter your choice here: ")
        if choice1 == "1":
            print(color.BOLD + "\nAlgebra 1\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: Algebra 1 Unit.\n" + color.END + link('https://www.khanacademy.org/math/algebra') + "\n")
            print(color.BOLD + "IXL: Algebra 1 Unit.\n" + color.END + link('https://www.ixl.com/math/algebra-1?_gl=1*1q6uawe*_up*MQ..&gclid=CjwKCAjwvKi4BhABEiwAH2gcw2-MjhLNuKEgu2z_hiaDZp2kY4NL4IU28g-ZdueVvqPMompVNAzz4RoCWM4QAvD_BwE') + "\n")
            print(color.BOLD + "MathPlanet Algebra 1 Unit.\n" + color.END + link('https://www.mathplanet.com/education/algebra-1') + "\n")
            #continue
        if choice1 == "2":
            print(color.BOLD + "\nGeometry\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: High School Geometry Unit.\n" + color.END + link('https://www.khanacademy.org/math/geometry') + "\n")
            print(color.BOLD + "IXl: Geometry Unit.\n" + color.END + link('https://www.ixl.com/math/geometry?_gl=1*tfo5sr*_up*MQ..&gclid=CjwKCAjwvKi4BhABEiwAH2gcw4lLk-MIKZELKNgoiXXd2eph1XUOG5esAR9h9TV-DF_KsaVbV4eljxoCBnQQAvD_BwE') + "\n")
            print(color.BOLD + "MathPlanet Geometry Unit.\n" + color.END + link('https://www.mathplanet.com/education/geometry') + "\n")
            #continue
        if choice1 == "3":
            print(color.BOLD + "\nAlgebra 2\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: Algebra 2 Unit.\n" + color.END + link('https://www.khanacademy.org/math/algebra2') + "\n")
            print(color.BOLD + "IXL: Algebra 2 Unit.\n" + color.END + link('https://www.ixl.com/math/algebra-2?_gl=1*n5qyjw*_up*MQ..&gclid=CjwKCAjwvKi4BhABEiwAH2gcw4lLk-MIKZELKNgoiXXd2eph1XUOG5esAR9h9TV-DF_KsaVbV4eljxoCBnQQAvD_BwE') + "\n")
            print(color.BOLD + "MathPlanet Algebra 2 Unit.\n" + color.END + link('https://www.mathplanet.com/education/algebra-2') + "\n")
        if choice1 == "4":
            print(color.BOLD + "\nPrecalculus\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: Precalculus Unit.\n" + color.END + link('https://www.khanacademy.org/math/precalculus') + "\n")
            print(color.BOLD + "IXL: Precalculus Unit.\n" + color.END + link('https://www.ixl.com/math/precalculus?_gl=1*q3ril2*_up*MQ..&gclid=CjwKCAjwvKi4BhABEiwAH2gcw4lLk-MIKZELKNgoiXXd2eph1XUOG5esAR9h9TV-DF_KsaVbV4eljxoCBnQQAvD_BwE') + "\n")
        if choice1 == "5":
            print(color.BOLD + "\nCalculus AB\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: AP Calculus AB Unit.\n" + color.END + link('https://www.khanacademy.org/math/ap-calculus-ab') + "\n")
            print(color.BOLD + "Khan Academy: Multivariable Calculus Unit.\n" + color.END + link('https://www.khanacademy.org/math/multivariable-calculus') + "\n")
            print(color.BOLD + "IXL: Calculus Unit.\n" + color.END + link('https://www.ixl.com/math/calculus?_gl=1*1gdqbov*_up*MQ..&gclid=CjwKCAjwvKi4BhABEiwAH2gcw4lLk-MIKZELKNgoiXXd2eph1XUOG5esAR9h9TV-DF_KsaVbV4eljxoCBnQQAvD_BwE') + "\n")
        if choice1 == "6":
            print(color.BOLD + "\nCalculus BC\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: AP Calculus BC Unit.\n" + color.END + link('https://www.khanacademy.org/math/ap-calculus-bc') + "\n")
            print(color.BOLD + "Khan Academy: Multivariable Calculus Unit.\n" + color.END + link('https://www.khanacademy.org/math/multivariable-calculus') + "\n")
            print(color.BOLD + "IXL: Calculus Unit.\n" + color.END + link('https://www.ixl.com/math/calculus?_gl=1*1gdqbov*_up*MQ..&gclid=CjwKCAjwvKi4BhABEiwAH2gcw4lLk-MIKZELKNgoiXXd2eph1XUOG5esAR9h9TV-DF_KsaVbV4eljxoCBnQQAvD_BwE') + "\n")
        if choice1 == "7":
            print(color.BOLD + "\nStatistics\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: High School Statistics Unit.\n" + color.END + link('https://www.khanacademy.org/math/probability') + "\n")
            print(color.BOLD + "Khan Academy: Statistics & Probability Unit.\n" + color.END + link('https://www.khanacademy.org/math/statistics-probability') + "\n")
            print(color.BOLD + "Khan Academy: AP Statistics Unit.\n" + color.END + link('https://www.khanacademy.org/math/ap-statistics') + "\n")
        if choice1 == "Q":
            break
    if choice == "2":
        choice2 = input("\nYou have selected: English Language Arts (ELA)\n1. High School Reading & Vocab.\n2. Grammar.\nEnter your choice here: ")
        if choice2 == "1":
            print(color.BOLD + "\nHigh School Reading & Vocab\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: 9th Grade Reading & Vocab Unit.\n" + color.END + link('https://www.khanacademy.org/ela/9th-grade-reading-and-vocabulary') + "\n")
            print(color.BOLD + "IXL: 9th Grade ELA Unit.\n" + color.END + link('https://www.ixl.com/ela/grade-9') + "\n")
            print(color.BOLD + "Khan Academy: 10th Grade Reading & Vocab Unit.\n" + color.END + link('https://www.khanacademy.org/ela/10th-grade-reading-and-vocabulary') + "\n")
            print(color.BOLD + "IXL: 10th Grade ELA Unit.\n" + color.END + link('https://www.ixl.com/ela/grade-10') + "\n")
            print(color.BOLD + "IXL: 11th Grade ELA Unit.\n" + color.END + link('https://www.ixl.com/ela/grade-11') + "\n")
            print(color.BOLD + "IXL: 12th Grade ELA Unit.\n" + color.END + link('https://www.ixl.com/ela/grade-12') + "\n")
        if choice2 == "2":
            print(color.BOLD + "\nGrammar\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: Grammar Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/grammar') + "\n")
            print(color.BOLD + "IXL: Grammar Unit.\n" + color.END + link('https://www.ixl.com/ela/topics?partner=google&campaign=179162755&adGroup=8821321675&gad_source=1&gclid=CjwKCAjwvKi4BhABEiwAH2gcwxrlUJPCEzlAMxhDiTWGl9X6RUbXDja0bx2plIhI9WJ9vxdNZ3wytRoCcXkQAvD_BwE') + "\n")
            print(color.BOLD + "Grammar Monster: Grammar Practice & Lessons.\n" + color.END + link('https://www.grammar-monster.com/index.html') + "\n")
        
    if choice == "3":
        choice3 = input("\nYou have selected: Sciences (Including Computer Sciences)\n1. Biology.\n2. Physics.\n3. Chemistry.\n4. Environmental Science.\n5. Computer Science.\nEnter your choice here: ")
        if choice3 == "1":
            print(color.BOLD + "\nBiology\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: High School Biology Unit.\n" + color.END + link('https://www.khanacademy.org/science/hs-bio') + "\n")
            print(color.BOLD + "IXL: Biology Unit.\n" + color.END + link('https://www.ixl.com/science/biology') + "\n")
            print(color.BOLD + "Khan Academy: AP Biology Unit.\n" + color.END + link('https://www.khanacademy.org/science/ap-biology') + "\n")
        if choice3 == "2":
            print(color.BOLD + "\nPhysics\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: High School Physics Unit.\n" + color.END + link('https://www.khanacademy.org/science/highschool-physics') + "\n")
            print(color.BOLD + "IXL: Physics Unit.\n" + color.END + link('https://www.ixl.com/science/physics') + "\n")
            print(color.BOLD + "Khan Academy: AP Physics Unit.\n" + color.END + link('https://www.khanacademy.org/science/ap-college-physics-1') + "\n")
        if choice3 == "3":
            print(color.BOLD + "\nChemistry\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: High School Chemistry Unit.\n" + color.END + link('https://www.khanacademy.org/science/hs-chemistry') + "\n")
            print(color.BOLD + "IXL: Chemistry Unit.\n" + color.END + link('https://www.ixl.com/science/chemistry') + "\n")
            print(color.BOLD + "Khan Academy: AP Chemistry Unit.\n" + color.END + link('https://www.khanacademy.org/science/ap-chemistry-beta') + "\n")
        if choice3 == "4":
            print(color.BOLD + "\nEnvironmental Sciences\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: AP Environmental Sciences Unit.\n" + color.END + link('https://www.khanacademy.org/science/ap-college-environmental-science') + "\n")
            print(color.BOLD + "IXL: Earth Sciences Unit\n" + color.END + link('https://www.ixl.com/science/earth-science') + "\n")
        if choice3 == "5":
            print(color.BOLD + "\nComputer Science\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: Introduction to CS with Python Unit.\n" + color.END + link('https://www.khanacademy.org/computing/intro-to-python-fundamentals') + "\n")
            print(color.BOLD + "Khan Academy: Computer Programming Unit.\n" + color.END + link('https://www.khanacademy.org/computing/computer-programming') + "\n")
            print(color.BOLD + "Khan Academy: AP Computer Science Principles Unit.\n" + color.END + link('https://www.khanacademy.org/computing/ap-computer-science-principles') + "\n")
  
    if choice == "4":
        choice4 = input("\nYou have selected: Histories (World, US), Economics, & Art\n1. US Histories.\n2. World Histories.\n3. Economics.\n4. Arts.\n5. Other Histories.\nEnter your choice here: ")
        if choice4 == "1":
            print(color.BOLD + "\nUS Histories & Government\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: US History Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/us-history') + "\n")
            print(color.BOLD + "Khan Academy: AP US History Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/ap-us-history') + "\n")
            print(color.BOLD + "Khan Academy: US Government & Civics Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/us-government-and-civics') + "\n")
            print(color.BOLD + "Khan Academy: AP US Government & Politics Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/ap-us-government-and-politics') + "\n")
        if choice4 == "2":
            print(color.BOLD + "\nWorld Histories\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: World History, Origins - Present Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/whp-origins') + "\n")
            print(color.BOLD + "Khan Academy: World History, 1750s - Present Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/whp-1750') + "\n")
            print(color.BOLD + "Khan Academy: World History Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/world-history') + "\n")
            print(color.BOLD + "Khan Academy: AP World History Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/world-history-project-ap') + "\n")
        if choice4 == "3":
            print(color.BOLD + "\nEconomics\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: Macroeconomics Unit.\n" + color.END + link('https://www.khanacademy.org/economics-finance-domain/macroeconomics') + "\n")
            print(color.BOLD + "Khan Academy: AP Macroeconomics Unit.\n" + color.END + link('https://www.khanacademy.org/economics-finance-domain/ap-macroeconomics') + "\n")
            print(color.BOLD + "Khan Academy: Microeconomics Unit.\n" + color.END + link('https://www.khanacademy.org/economics-finance-domain/microeconomics') + "\n")
            print(color.BOLD + "Khan Academy: AP Microeconomics Unit.\n" + color.END + link('https://www.khanacademy.org/economics-finance-domain/ap-microeconomics') + "\n")
        if choice4 == "4":
            print(color.BOLD + "\nArts Histories\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: Art History Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/art-history') + "\n")
            print(color.BOLD + "Khan Academy: AP Art History Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/ap-art-history') + "\n")
        if choice4 == "5":
            print(color.BOLD + "\nOther Histories\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: Constitution 101 Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/constitution-101') + "\n")
            print(color.BOLD + "Khan Academy: Big History Project Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/big-history-project') + "\n")
            print(color.BOLD + "Khan Academy: Climate Project Unit.\n" + color.END + link('https://www.khanacademy.org/humanities/climate-project') + "\n")
    if choice == "5":
        choice5 = input("\nYou have selected: Standardized Testing Prep Materials\n1. SAT.\n2. ACT.\nEnter your choice here: ")
        if choice5 == "1":
            print(color.BOLD + "\nSAT Prep\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nKhan Academy: Digital SAT Unit.\n" + color.END + link('https://www.khanacademy.org/digital-sat') + "\n")
            print(color.BOLD + "Manhattan Review: SAT Prep Unit.\n" + color.END + link('https://www.manhattanreview.com/free-sat-practice-questions/') + "\n")
        if choice5 == "2":
            print(color.BOLD + "\nACT Prep\n" + color.END)
            print("Here are some resources available which are free of charge!\n")
            print(color.BOLD + "\nACT Website: ACT Practice Test.\n" + color.END + link('https://www.act.org/content/act/en/products-and-services/the-act/test-preparation/free-act-test-prep.html') + "\n")
            print(color.BOLD + "ACT Website: Prepare for the ACT.\n" + color.END + link('https://www.act.org/content/act/en/products-and-services/the-act/test-preparation.html') + "\n")
            print(color.BOLD + "Kaptest: ACT Practice Test & Questions.\n" + color.END + link('https://www.kaptest.com/act/free/act-free-practice-test?srsltid=AfmBOoqPyyqOBT1vtd6kGGl1VNYPo7TLeAadj_lRYYR5FarNLuPsPwCQ') + "\n")
    #else:
        #print("Please try again. You have entered an invalid choice.\n")

'''
print(color.BOLD + "\n\n" + color.END)
print("Here are some resources available which are free of charge!\n")
print(color.BOLD + "\n\n" + color.END + link('') + "\n")
print(color.BOLD + "\n" + color.END + link('') + "\n")
print(color.BOLD + "\n" + color.END + link('') + "\n")
print(color.BOLD + "\n" + color.END + link('') + "\n")

'''