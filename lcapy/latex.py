import re

pattern = re.compile(r"([_\^]){([\w]+)}")


class Latex(object):

    words = ('in', 'out', 'ref', 'rms', 'load', 'source', 'avg',
             'mean', 'peak', 'pp', 'min', 'max', 'src',
             'cc', 'ee', 'dd', 'ss', 'ih', 'il', 'oh', 'ol')

    def __init__(self, string):

        self.str = string

    def mathrm(self):
        """Place words in sub- or super-scripts inside a mathrm.
        For example V_{rms} -> V_{\mathrm{rms}}"""
        
        
        def foo(match):
            
            fred = match.group(2)
            
            if fred.lower() in self.words:
                fred = r'{\mathrm{%s}}' % fred
            else:
                fred = r'{%s}' % fred
            return match.group(1) + fred

        return pattern.sub(foo, self.str)

    def __str__(self):
        
        return self.mathrm()


def latex_str(string):

    return Latex(string).__str__()


def format_label(s):

    if s == '':
        return s
    # Pass math-mode labels verbatim.
    if s[0] == '$' and s[-1] == '$':
        return s
    # With leading $ and no trailing $, e.g., v=$V1, try to
    # automagically convert to LateX string, otherwise pass
    # verbatim.  Currently, this only converts words in sub- or
    # super- scripts to roman. TODO, handle more cases.
    if s[0] == '$' and s[-1] != '$':
        return '$' + latex_str(s[1:]) + '$'
    # If have + or ^ need to be in math-mode.
    if '_' in s or '^' in s:
        return '$' + latex_str(s) + '$'
    return s

