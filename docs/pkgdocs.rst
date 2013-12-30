
================
Package Metadata
================

- **classifier**:: 

    Intended Audience :: Science/Research
    Topic :: Scientific/Engineering

- **description-file:** README.txt

- **entry_points**:: 

    [openmdao.variable]
    analysis_server.proxy.EnumProxy=analysis_server.proxy:EnumProxy
    analysis_server.proxy.ListProxy=analysis_server.proxy:ListProxy
    analysis_server.proxy.BoolProxy=analysis_server.proxy:BoolProxy
    analysis_server.proxy.IntProxy=analysis_server.proxy:IntProxy
    analysis_server.proxy.StrProxy=analysis_server.proxy:StrProxy
    analysis_server.proxy.ArrayProxy=analysis_server.proxy:ArrayProxy
    analysis_server.proxy.FloatProxy=analysis_server.proxy:FloatProxy
    analysis_server.proxy.FileProxy=analysis_server.proxy:FileProxy
    [openmdao.component]
    analysis_server.test.OptComps.RosenSuzuki.RosenSuzuki=analysis_server.test.OptComps.RosenSuzuki:RosenSuzuki
    analysis_server.proxy.ComponentProxy=analysis_server.proxy:ComponentProxy
    analysis_server.test.ASTestComp.TestComponent=analysis_server.test.ASTestComp:TestComponent
    analysis_server.test.test_proxy.Sink=analysis_server.test.test_proxy:Sink
    analysis_server.test.test_proxy.Source=analysis_server.test.test_proxy:Source
    analysis_server.test.test_proxy.Model=analysis_server.test.test_proxy:Model
    [openmdao.container]
    analysis_server.proxy.ObjProxy=analysis_server.proxy:ObjProxy
    analysis_server.test.OptComps.RosenSuzuki.RosenSuzuki=analysis_server.test.OptComps.RosenSuzuki:RosenSuzuki
    analysis_server.proxy.ComponentProxy=analysis_server.proxy:ComponentProxy
    analysis_server.test.ASTestComp.SubObj=analysis_server.test.ASTestComp:SubObj
    analysis_server.test.ASTestComp.TopObj=analysis_server.test.ASTestComp:TopObj
    analysis_server.test.test_proxy.Sink=analysis_server.test.test_proxy:Sink
    analysis_server.test.ASTestComp.SubGroup=analysis_server.test.ASTestComp:SubGroup
    analysis_server.test.ASTestComp.TestComponent=analysis_server.test.ASTestComp:TestComponent
    analysis_server.test.test_proxy.Source=analysis_server.test.test_proxy:Source
    analysis_server.test.test_proxy.Model=analysis_server.test.test_proxy:Model

- **keywords:** openmdao

- **name:** analysis_server

- **requires-dist:** openmdao.main

- **requires-python**:: 

    >=2.6
    <3.0

- **static_path:** [ '_static' ]

- **summary:** OpenMDAO interface to Phoenix Integration's ModelCenter/AnalysisServer

- **version:** 0.5.2

