# Parse_ruby_project

This is a simple ​Python command line application for UNIX-like environments which, given a source code folder, finds out all Ruby files in there, parses them through and produces a list of ​internal file-level dependencies. (i.e. file A has a dependency on file B)  
 

## Usage

The program is run like this: 

```bash
python3 parse_ruby.py {PATH_OF_RUBY_PROJECT}
```

Once done, your program will output the following files:

```bash
- sample-ruby-project_internal_deps.list 
- sample-ruby-project_external_deps.list 
```   

## License
[MIT](https://choosealicense.com/licenses/mit/)