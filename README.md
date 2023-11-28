# Marvel-Universe

Marvel Universe is an engaging web application tailored for passionate Marvel enthusiasts. Dive into the captivating
world of Marvel's iconic characters, series, and comics. Share your opinions in the dedicated sections for series and
comics, where your thoughts come to life. Additionally, explore real-world locations inspired by the Marvel universe and
share fascinating insights about these places.

## Install and Configure the Application

[Installation Guide](installation.md)

###### Running the Application (if python doesn't work use python3 instead)

1. Clone repository from github

    ```
   git clone https://github.com/Marvel-Universe/MarvelUniverse2.git
   ```
2. Access to the project directory.
   ```
   cd MarvelUniverse
   ```
3. Create a Virtual Environment.
   ```
   python -m venv venv
   ```
   On Windows:
   ```
   venv\Scripts\activate
   ```
   On macOS and Linux:
   ```
   source venv/bin/activate
   ```

4. Install Dependencies

    ```
   pip install -r requirements.txt
   ```

5. Create .env file and set values for externalized variables following sample.env in the repository.

6. Set Up the Database.
   ```
   python manage.py migrate
   ```

7. Download data.
   ```
   python manage.py loaddata data/*.json
   ```

8. Run the server.
   ```
   python manage.py runserver
   ```

### Project documents
- [Vision Statement](https://github.com/Marvel-Universe/MarvelUniverse.wiki.git)
- [Requirements](https://github.com/Marvel-Universe/MarvelUniverse.wiki.git)
- [Development Plan](https://github.com/Marvel-Universe/MarvelUniverse.wiki.git)
- [User stories](https://github.com/Marvel-Universe/MarvelUniverse.wiki.git)
- [Domain model](https://miro.com/app/board/uXjVNdOa0Qo=/?share_link_id=514388665087)
- [Website Mock-up](https://www.figma.com/file/Wvt65InqZ3Gp9CX9xlUDHp/Marvel-Universe?type=design&node-id=0-1&mode=design)
- [Project Board](https://github.com/orgs/Marvel-Universe/projects/4)

### Design Documents
* [Website Mock-up](https://www.figma.com/file/Wvt65InqZ3Gp9CX9xlUDHp/Marvel-Universe?type=design&node-id=0%3A1&mode=design&t=7plgw6rFLkbc505V-1)
* [Domain model](https://miro.com/app/board/uXjVNdOa0Qo=/?share_link_id=514388665087)
* [[Class Diagram]]
* [[Sequence Diagram]]
* [Project Proposal Slide](https://www.canva.com/design/DAFwCO9Yhec/qyE5YoVGWvG7u55OwDyo7w/edit)

### Iteration Plan
- [Iteration 1 Plan](https://github.com/Marvel-Universe/MarvelUniverse/wiki/Iteration-1) and [Task Board](https://github.com/orgs/Marvel-Universe/projects/4/views/2)
- [Iteration 2 Plan](https://github.com/Marvel-Universe/MarvelUniverse/wiki/Iteration-2) and [Task Board](https://github.com/orgs/Marvel-Universe/projects/4/views/3)
- [Iteration 3 Plan](https://github.com/Marvel-Universe/MarvelUniverse/wiki/Iteration-3) and [Task Board](https://github.com/orgs/Marvel-Universe/projects/4/views/4)
- [Iteration 4 Plan](https://github.com/Marvel-Universe/MarvelUniverse/wiki/Iteration-4) and [Task Board](https://github.com/orgs/Marvel-Universe/projects/4/views/5)
- [Iteration 5 Plan](https://github.com/Marvel-Universe/MarvelUniverse/wiki/Iteration-5) and [Task Board](https://github.com/orgs/Marvel-Universe/projects/4/views/6)
- [Iteration 6 Plan](https://github.com/Marvel-Universe/MarvelUniverse/wiki/Iteration-6) and [Task Board](https://github.com/orgs/Marvel-Universe/projects/4/views/7)
- [Iteration 7 Plan](https://github.com/Marvel-Universe/MarvelUniverse/wiki/Iteration-7) and [Task Board](https://github.com/orgs/Marvel-Universe/projects/4/views/8)
- [Iteration 8 Plan](https://github.com/Marvel-Universe/MarvelUniverse/wiki/Iteration-8) and [Task Board](https://github.com/orgs/Marvel-Universe/projects/4/views/9)
- [Iteration 9 Plan](https://github.com/Marvel-Universe/MarvelUniverse/wiki/Iteration-9) and [Task Board](https://github.com/orgs/Marvel-Universe/projects/4/views/10)
