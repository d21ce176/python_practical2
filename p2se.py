#Write a Python program to find the most common elements and their counts from set, tuple, dictionary.
def common(arr1,arr2,arr3):
    s1=set(arr1)
    s2=set(arr2)
    s3=set(arr3)
    print('list=',arr1)
    print('tupple=',arr2)
    print('dict=',arr3)
    set1=s1.intersection(s2)
    result_set=set1.intersection(s3)
    final_list=set(result_set)
    print('common element:',final_list)

    if_name_=='__main__'
    list1=[1,2,'ABC','xyz']
    tuple=(80,90,'ABC','xyz')
    dict={300,400,'ABC','xyz'} 
    common(list1,tuple,dict)
    print("this program is prepared by om and id :d21ce176")  