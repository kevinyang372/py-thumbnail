import re
from .rulegroup import RuleGroup
from .parsing import Parsing

class thumbnail:

    def __init__(self, directory, silence, keys):

        self.filename = directory.split('/')[-1]

        if self.filename == '':
            raise "Please input directory in the correct format"

        with open (directory, "r") as myfile:
            self.data = myfile.readlines()

        self.summary = None
        self.tree = RuleGroup(None, 'File', -1, True)
        self.keys = ['class', 'def', 'for', 'if', 'elif', 'else:', 'while']
        self.print_keys = keys
        self.silence = silence

    def __detect_group(self, string, group_level):
        k = string[group_level:].split()
        if not len(k) == 0 and k[0] in self.keys:
            return k[0]
        else:
            return None

    def __check_group_level(self, string):
        level = 0 
        while level < len(string) and string[level] == ' ' or string[level] == '\t':
            level += 1
        return level

    def scan(self):
        group_level = 0
        self.tree = RuleGroup(None, 'File', -1, True)
        self.tree.functionname = self.filename
        self.summary = {'class': 0, 'def': 0, 'for': 0, 'if': 0, 'while': 0}
        
        group_parent = [(-1, self.tree)]
        token_tree = []
        
        for i in self.data:
            
            if i == '\n':
                continue
            
            group_level = self.__check_group_level(i)
            
            for t in range(len(group_parent)):
                if group_parent[t][0] >= group_level:
                    group_parent = group_parent[:t]
                    break
                    
            check = self.__detect_group(i, group_level)
            
            if not check is None:
                
                if check in self.summary:
                    self.summary[check] += 1
                
                r = RuleGroup(group_parent[-1], check, group_level, check in self.print_keys)
                p = Parsing(i[group_level + len(check) + 1:], r, self.silence)
                p.run()
                token_tree.append(r)
                group_parent.append((group_level, r))
                
                group_parent[-2][1].child.append(r)

    def search(self, name, start = None):

        if start is None:
            start = self.tree

        result = None

        for i in start.child:
            if i.functionname == name:
                return i
            result = self.search(name, start = i)

        return result

    def show_summary(self):
        if self.summary is None:
            raise("Run scan function first to get summary information")
        for i in self.summary:
            print(i, ': ', self.summary[i])
        return self.summary

    def show_text(self):
        return self.data
