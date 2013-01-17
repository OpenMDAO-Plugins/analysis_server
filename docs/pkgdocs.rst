
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
    analysis_server.proxy.BoolProxy=analysis_server.proxy:BoolProxy
    analysis_server.proxy.IntProxy=analysis_server.proxy:IntProxy
    analysis_server.proxy.StrProxy=analysis_server.proxy:StrProxy
    analysis_server.proxy.ArrayProxy=analysis_server.proxy:ArrayProxy
    analysis_server.proxy.FloatProxy=analysis_server.proxy:FloatProxy
    analysis_server.proxy.ListProxy=analysis_server.proxy:ListProxy
    analysis_server.proxy.FileProxy=analysis_server.proxy:FileProxy
    [openmdao.component]
    analysis_server.proxy.ComponentProxy=analysis_server.proxy:ComponentProxy
    [openmdao.container]
    analysis_server.proxy.ObjProxy=analysis_server.proxy:ObjProxy
    analysis_server.proxy.ComponentProxy=analysis_server.proxy:ComponentProxy

- **keywords:** openmdao

- **name:** analysis_server

- **requires-dist:** openmdao.main

- **requires-python**:: 

    >=2.6
    <3.0

- **static_path:** [ '_static' ]

- **summary:** OpenMDAO interface to Phoenix Integration's ModelCenter/AnalysisServer

- **version:** 0.1

