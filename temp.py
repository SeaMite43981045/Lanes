class Template:
    def template_detect(self, text: str, **kwargs):
        if len(kwargs) > 0:
            kd = {}
            kl = []
            load = False

            for s in range(len(text)):
                if text[s] == "{" and text[s+1] == "{":
                    k, rk = "", ""
                    load = True
                if text[s-1] == "}" and text[s] == "}":
                    rk += '}'
                    kl.append(k)
                    kd[k] = [rk, kwargs[k]]
                    load = False
                if load:
                    if text[s] != '{' and text[s] != '}' and text[s] != ' ':
                        k += text[s]
                    rk += text[s]
            for w in kl:
                text = text.replace(kd[w][0], kd[w][1])
            return text
        else:
            return text