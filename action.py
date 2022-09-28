def Valeus(self, *args):
        for i in range (1,19):
            fun1 = f"self.v{i} = self.ent{i}.get()"
            funx1 = exec(fun1) 
            fun5 = f"s{i} = string_to_crc(v{i})"
            funx5 = exec(fun5) 
            #fun3 = f"s{i} = ans"
            #funx3 = exec(fun3)
            fun2 = f"self.sort{i}.delete(0,'end')"
            funx2 = exec(fun2)
            fun4 = f"self.sort{i}.insert(0,self.s{i})"
            funx4 = exec(fun4)