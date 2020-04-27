# Harry Parser and the Sourcerer's Feeds

[![Build Status](https://travis-ci.com/Jhawk1196/CS3250PythonProject.svg?branch=master)](https://travis-ci.com/Jhawk1196/CS3250PythonProject)




This python 3 program parses RSS feeds and displays them at rotating frequency in a small window. As the feeds rotate 


The feeds may be provided in a few different ways as outlined below:

1. By url of RSS feed:

    `python main.py --url "http://rss.cnn.com/rss/cnn_us.rss"`
    
2. In a static file:

    `python main.py --file "json_file_with_links.json"`
    
3. In a .yaml/.yml file:
    
    `python main.py --config "yaml_configuration.yml"`
    
    .yaml/.yml files should have a structure following that of the accompanying default_config.yml.
    All of those fields are optional.
    
    
##### You need to install Visual Studio C++ 14.0 for lxml to import and download.