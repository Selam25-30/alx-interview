# :book: 0x09. Island Perimeter.
## :page_with_curl: Topics Covered.
Island Perimeter interview question.
# :computer: Tasks.
<!---->
## [0. Island Perimeter](0-island_perimeter.py)
### :page_with_curl: Task requirements.
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

* `grid` is a list of list of integers:
    * 0 represents water
    * 1 represents land
    * Each cell is square, with a side length of 1
    * Cells are connected horizontally/vertically (not diagonally).
    * `grid` is rectangular, with its width and height not exceeding 100
* The grid is completely surrounded by water
* There is only one island (or nothing).
* The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
```
    guillaume@ubuntu:~/0x09$ cat 0-main.py
    #!/usr/bin/python3
    """
    0-main
    """
    island_perimeter = __import__('0-island_perimeter').island_perimeter
    
    if __name__ == "__main__":
        grid = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        print(island_perimeter(grid))
     
```
**Repo:**

* GitHub repository: `alx-interview`
* Directory: `0x09-island_perimeter`
* File: `0-island_perimeter.py`
### :wrench: Task setup.
```bash
# Create solution file.
touch 0-island_perimeter.py
chmod +x 0-island_perimeter.py

# Lint.
pep8 0-island_perimeter.py

# Test.
touch 0-main.py
chmod +x 0-main.py
./0-main.py
```
# :man: Author and Credits.
This project was done by [SE. Moses Mwangi](https://github.com/Endale24). Feel free to get intouch with me;

:email: Email [endale2400@gmail.com](endale2400@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.