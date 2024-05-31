from cumulonimbus_models.system import Software, SoftwareInstallationMethod, SystemInfo, SystemUpdateRequest


def test_system():
    assert SystemUpdateRequest(
        system_info=SystemInfo(
            os='test',
            hostname='test',
            software=[
                Software(
                    name='test',
                    version='test',
                    installation_method=SoftwareInstallationMethod.PIP,
                    installation_data={'test': 'test'},
                    config_data={'test': 'test'}
                )
            ]
        )
    )