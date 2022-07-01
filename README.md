## The what

A small python code snippet for displaying XLS files in your shell.

## The why

Clients usually send me an encrypted archive with an XLS file containing credentials for starting a pentest.

I got tired of switching to GUI.

## The how

1. Meet the dependencies

```
python3 -m pip install -r requirements.txt
```

2. Make a quick and dirty install

```
chmod +x xls2txt.py
sudo cp xls2txt.py /usr/local/bin/ 
```

3. Profit?

```
$> xls2txt.py -h         
usage: xls2txt.py [-h] -f FILE

An XLS reader for your shell, because I had a use for it.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  your XLS file, what else?

From @_erk3_ with love
```

![demo](/example/demo.png)
