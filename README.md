# LEOURA  AN INDIE GAME PLATFORM
## INTRODUCTION 

We have built a indie arcade game platform that can support multiple indie games .The platform supports multiplayer play across two players for a particular game . the platform features a leaderboard that gets updated automatically based on a play. The platform also suppports exporting the dat and importing the saved data.
This project is a tribute to all the indie game devs who work tirelessly for the game dev community .


Build | Code Quality |  Unity| Git Inspector| Code Coverage | Codacy
|---------|------------|-------------------------|-----------|----------------|----------------|
|[![C/C++ CI - Build Status](https://github.com/joydeep2899/260212_miniproject/actions/workflows/c-cpp.yml/badge.svg?branch=main&event=push)](https://github.com/joydeep2899/260212_miniproject/actions/workflows/c-cpp.yml)[![C/C++ CI WINDOWS- Build Status](https://github.com/joydeep2899/260212_miniproject/actions/workflows/windows.yml/badge.svg?branch=main&event=push)](https://github.com/joydeep2899/260212_miniproject/actions/workflows/windows.yml)|[![Code Quality - Static Code - Cppcheck](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-cppcheck.yml/badge.svg?branch=main&event=push)](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-cppcheck.yml)[![CodeQuality Dynamic Code Analysis Valgrind](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-dynamic-code-quality.yml/badge.svg?branch=main&event=push)](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-dynamic-code-quality.yml)|[![Unit Testing - Unity](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-unity.yml/badge.svg?branch=main&event=push)](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-unity.yml)|[![Contribution Check - Git Inspector](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-gitinspector.yml/badge.svg?branch=main&event=push)](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-gitinspector.yml)|[![CI-Coverage](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-code-coverage.yml/badge.svg?branch=main&event=push)](https://github.com/joydeep2899/260212_miniproject/actions/workflows/arc-code-coverage.yml)|[![Codacy Badge](https://app.codacy.com/project/badge/Grade/373088c121f7423695121e001e701408)](https://www.codacy.com/gh/joydeep2899/260212_miniproject/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=joydeep2899/260212_miniproject&amp;utm_campaign=Badge_Grade)










## Folder Structure
Folder             | Description
-------------------| -----------------------------------------
`1_Requirements`   | Documents detailing requirements and research
`2_Architecture`         | Documents specifying design details
`3_Implementation` | All code and documentation
`4_Test_plan and output`      | Documents with test plans and procedures
`5_Report`      | Documents containing project report
`6_Images and videos `      | Images and videos related to project 
`7_Other`      | other miscellaneous files 

## Contributors List and Summary

SF Id. | | Name   |    Features    | Issuess Raised |Issues Resolved|No Test Cases|Test Case Pass
-------|--|-------|----------------|----------------|---------------|-------------|--------------
`260212`| `99004391`  | Joydeep Ghosh  | 1,2,3,4,5,6  | 3     | 3   |1   |1    
   
## List  Of Features 
| Feature Id | Feature |
| -----------:|---------:|
|F1| Leaderboard |
|F2| add or remove games easily |
|F3| export and import data |
|F4| system works on all platforms |
|F5| multiplayer |



## Challenges Faced and How Was It Overcome
| No. | Challenge | Solution
|-----|-----------|--------
|1. | Code Crashed without any error message (Segmentation Fault) | valgrind helped find that minheap address was not being returned 
|2. | huffman tree was not getting built correctly | Implemented minheap |
|3. | minheap was not getting created directly from array | implemented heapnode data structure 
|4. | huffman tree was not getting printed on screen  | wrote printhuffman code to traverse the huffman tree and print huffman codes for each leaf node 
|5. | code coverage was not 100%  |  gcov helped find variable status was not intialised but not used and therefore it was deleted 
