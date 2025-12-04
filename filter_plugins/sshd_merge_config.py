DELETE_MARKERS = [ "_", "-" ]

def sshd_merge_config(base_config, override_config, delete_markers=None):
    if delete_markers is None:
        delete_markers = DELETE_MARKERS

    delete_targetkeys = []
    for key in override_config.keys():
        for marker in delete_markers:
            if key.startswith(marker):
                delete_targetkeys.append(key[len(marker):])
                break

    merged = {
        key: value
        for key, value in base_config.items()
        if key not in delete_targetkeys
    }

    overrides = {}
    for key, value in override_config.items():
        is_delete_marker = any(key.startswith(marker) for marker in delete_markers)
        if not is_delete_marker:
            overrides[key] = value

    merged.update(overrides)
    return merged


class FilterModule(object):
    def filters(self):
        return {
            'sshd_merge_config': sshd_merge_config,
        }
