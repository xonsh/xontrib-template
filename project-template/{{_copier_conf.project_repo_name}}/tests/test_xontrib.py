def test_it_loads(load_xontrib):
    load_xontrib("{{ _copier_conf.project_package_name }}")
