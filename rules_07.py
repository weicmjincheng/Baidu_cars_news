import nltk, json
from .tools import ner_stanford

keep_pos = "q,qg,qt,qv,s,t,tg,g,gb,gbc,gc,gg,gm,gp,m,mg,Mg," \
           "mq,n,an,vn,ude1,nr,ns,nt,nz,nb,nba,nbc,nbp,nf,ng," \
           "nh,nhd,o,nz,nx,ntu,nts,nto,nth,ntch,ntcf,ntcb,ntc,nt," \
           "nsf,ns,nrj,nrf,nr2,nr1,nr,nnt,nnd,nn,nmc,nm,nl,nit,nis," \
           "nic,ni,nhm,nhd"
keep_pos_nouns = set(keep_pos.split(","))
keep_pos_v = "v,vd,vg,vf,vl,vshi,vyou,vx,vi"
keep_pos_v = set(keep_pos_v.split(","))
keep_pos_p = set(['p', 'pbei', 'pba'])


def get_stanford_ner_nodes(parent):
    # date = ''
    org = ''
    loc = ''
    for node in parent:
        if type(node) is nltk.Tree:
            # if node.label() == 'DATE':
            #     date = date + " " + ''.join([i[0] for i in node])

            if node.label() == 'ORGANIZATIONL':
                org = org + " " + ''.join([i[0] for i in node])
            elif node.label() == 'LOCATION':
                loc = loc + " " + ''.join([i[0] for i in node])
    if len(org) > 0 or len(loc) > 0:
        # 'date': date,
        return { 'org': org, 'loc': loc}
    else:
        return {}

# 使用nltk对名词短语进行分块
def grammer_parse(raw_sentence=None, file_object=None):
    if len(raw_sentence.strip()) < 1:
        return False
    grammer_dict = \
        {

            'stanford_ner_drop': r"""
        DATE:{<DATE>+<MISC>?<DATE>*}
        {<DATE>+<MISC>?<DATE>*}
        {<DATE>+}
        {<TIME>+}
        ORGANIZATIONL:{<ORGANIZATION>+}
        LOCATION:{<LOCATION|STATE_OR_PROVINCE|CITY|COUNTRY>+}
        """
        }
    # 正则表达式分块器
    stanford_ner_drop_rp = nltk.RegexpParser(grammer_dict['stanford_ner_drop'])
    try:
        # parse后得到的类似于树状
        stanford_ner_drop_result = stanford_ner_drop_rp.parse(ner_stanford(raw_sentence))

    except:
        print("the error sentence is {}".format(raw_sentence))
    else:
        # 调用get_stanford_ner_nodes方法对名词短语进行分块
        stanford_keep_drop_dict = get_stanford_ner_nodes(stanford_ner_drop_result)
        if len(stanford_keep_drop_dict) > 0:

            # separators参数的作用是去掉,,:后面的空格，从上面的输出结果都能看到”, :”
            # 后面都有个空格，这都是为了美化输出结果的作用，但是在我们传输数据的过程中，越精简越好，冗余的东西全部去掉，因此就可以加上.
            # skipkeys参数，在encoding过程中，dict对象的key只可以是string对象，如果是其他类型，那么在编码过程中就会抛出ValueError的异常。
            # skipkeys可以跳过那些非string对象当作key的处理.
            # 输出真正的中文需要指定ensure_ascii=False
            file_object.write(json.dumps(stanford_keep_drop_dict, skipkeys=False,
                                         ensure_ascii=False,
                                         check_circular=True,
                                         allow_nan=True,
                                         cls=None,
                                         indent=4, # indent参数根据数据格式缩进显示，读起来更加清晰。
                                         separators=None,
                                         default=None,
                                         sort_keys=False)) # sort_keys是告诉编码器按照字典排序(a到z)输出。
