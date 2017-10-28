Install virtualenv:

    pip install virtualenv

create your virtual environment:

    virtualenv venv

activate your virtual environment:

    source venv/bin/activate

Now you are working inside a virtual environment and you'll be able to install
new dependencies without having to worry about breaking system configuration or
dependencies.


install the dependencies:

    pip install -r requirements.txt

Now you can run your spider because `Scrapy` was installed:

1. Move into the `crawler` directory:

       cd crawler

2. Run the spider:

       scrapy crawl stackoverflow


Now run the plot script to check tech trending for remote jobs in stackoverflow:

    python plot.py