#!/usr/bin/env python3


import os, sys, configparser, subprocess
from tempfile import TemporaryFile


def error (reasons):
    print("error")
    for r in reasons:
        print(r)
    print("exiting")
    sys.exit(0) 

    
def page_error (reasons):
    print("error")
    for r in reasons:
        print("\t"+r)
    return


def parse_config ():
    print("checking config.ini... ", end = '')
    missing = []
    config = configparser.ConfigParser()

    if os.path.isfile('./config.ini'):
        config.read('./config.ini')
    else:
        error(["config.ini is missing from this directory"])
    if 'default' not in config:
        error(["[default] section missing from config.ini"])

    keys = ['layouts', 'site', 'matter', 'domain']
    for key in keys:
        if key not in config['default']:
            missing.append("\"%s\" key missing from config.ini" % key)
    if missing:
        error(missing)

    conf = {}
    for key in keys:
        conf[key] = config['default'][key]
         
    print("done")
    return conf


def find_markdown (root):
    print("finding markdown files... ", end = '')
    md = []
    for dirName, subdirList, fileList in os.walk(root):
        for fname in fileList:
            if fname.endswith(".md"):
                md.append((dirName+"/"+fname)[len(root):-3])
    print("done")
    return md


def generate_website (f, conf):
    html_file = conf['site'] + f + ".html"
    if os.path.isfile(html_file):
        print("updating ", end = '')
    else:
        print("creating ", end = '')
    print ("website.com" + f + ".html... ", end = '')

    md_file, tag = parse_markdown(conf['matter'] + f + ".md")

    if tag['layout']:
        layout = conf['layouts'] + "/" + tag['layout']
        if os.path.isfile(layout):
           print("correct layout syntax")
           # layout_tags = find_tags(layout)
    # else:
        # just build the markdown

    # remove html page
    # build page

    print("done")


def parse_markdown (markdown_file):
    md_file = TemporaryFile()
    md = open(markdown_file,"r")
    tag = {}
    for ln in md:
        if ln.startswith("@"):
            try:
                i = ln[1:-1].split(': ')
                tag[i[0]] = i[1]
            except:
                error(["\""+i[0]+"\" variable in "+markdown_file+" formatted incorrectly"])
        else:
            md_file.write(bytes(ln, 'UTF-8'))

    #tags = infer_tags(md_file, tags)

    return md_file, tag


def main ():
    conf = parse_config()
    files = find_markdown(conf['matter'])
    for f in files:
        generate_website(f, conf)
    print("finished successfully")


if __name__ == "__main__":
    main()
