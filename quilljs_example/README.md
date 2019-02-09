# django-quill Example Project


### Running Development Server

1. install virtualenv

    ```bash
    $ make install
    ```
2. Activate virtual env
    ```bash
    $ source .venv/bin/activate
    ```

3. Install quilljs

    ```bash
    $ python setup.py develop
    ```

4. Sync Database and create superuser

    ```bash
    $ cd quilljs_example
    $ python manage.py migrate
    $ python manage.py createsuperuser
    ```

5. Run development server

    ```bash
    $ cd django-quilljs
    $ python manage.py runserver
    ```

6. In another console window, build django-quilljs:

    ```bash
    $ make watch
    ```

7. The example project will be available at http://localhost:8000.
