queries = QuerySet(object_provides__allof=['zopen.apps.interfaces.ISuperApplet'], parent=getRoot(context))
apps=[]
for app in queries:
    if app.related_package ==u'zopen.review':
        apps.append(app)
flows = QuerySet(object_provides__anyof=['zopen.model.interfaces.IDataItem']).filter(path__anyof=apps)
for flow in flows:
    if IFlowTasksManager(flow).listCurrentTasks()[0].title == u'ARC，PLM approve':
        flow['step'] =PersistentList(['[ARC，PLM approve]:'])[0]
        app_task = IFlowTasksManager(flow).listCurrentTasks()[0]
        IDublinCore(app_task).title = u'[ARC，PLM approve]:'
    if IFlowTasksManager(flow).listCurrentTasks()[0].title == u'SW，QA，PLM，ARC，DOC，TME评审':
        flow['step'] =PersistentList(['[SW，QA，PLM，ARC，DOC，TME评审]:'])[0]
        app_task = IFlowTasksManager(flow).listCurrentTasks()[0]
        IDublinCore(app_task).title = u'[SW，QA，PLM，ARC，DOC，TME评审]:'
    if IFlowTasksManager(flow).listCurrentTasks()[0].title == u'归档':
        flow['step'] =PersistentList(["[归档]:"])[0]
        app_task = IFlowTasksManager(flow).listCurrentTasks()[0]
        IDublinCore(app_task).title = u'[归档]:'
    if IFlowTasksManager(flow).listCurrentTasks()[0].title == u'SW,ARC,QA评审':
        flow['step'] =PersistentList(["[SW,ARC,QA评审]:"])[0]
        app_task = IFlowTasksManager(flow).listCurrentTasks()[0]
        IDublinCore(app_task).title = u'[SW,ARC,QA评审]:'
    if IFlowTasksManager(flow).listCurrentTasks()[0].title == u'DOC人员评审':
        flow['step'] =PersistentList(['[DOC人员评审]:'])[0]
        app_task = IFlowTasksManager(flow).listCurrentTasks()[0]
        IDublinCore(app_task).title = u'[DOC人员评审]:'
    if IFlowTasksManager(flow).listCurrentTasks()[0].title == u'SW，QA评审':
        flow['step'] =PersistentList(['[SW，QA评审]:'])[0]
        app_task = IFlowTasksManager(flow).listCurrentTasks()[0]
        IDublinCore(app_task).title = u'[SW，QA评审]:'
    reviewers = PersistentList([])
    for item in ISettings(container)['steps']:
        if item['responsible'] == 'handwork':
            reviewers.append(PersistentDict({'step':item['title']}))
    for i in range(len(reviewers)):
        context['reviewers'][i].update(reviewers[0])
