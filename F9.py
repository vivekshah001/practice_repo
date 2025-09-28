# write a generator function that yeild even numbers up to a specified limit.



def even_gene(limit):
    for i in range(2,limit+1,2):
        print(i)
even_gene(10)