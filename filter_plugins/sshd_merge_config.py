DEFAULT_MARKERS = ["_", "-", "#"]


def sshd_merge_config(base_config, override_config, delete_markers=None):
    """
    Merge configuration and process keys/values with deletion markers.

    Deletion rules:
    1. Key level: '_KeyName' → removes 'KeyName' from base_config
    2. Value level (list):
       - '_value' → removes 'value' from the corresponding list in base_config
       - '-value' → removes 'value' from the corresponding list in base_config
       - '#value' → removes 'value' from the corresponding list in base_config

    Args:
        base_config: Base configuration dictionary
        override_config: Override configuration dictionary
        delete_markers: List of deletion markers (default: ["_", "-", "#"])

    Returns:
        Merged configuration dictionary
    """
    if delete_markers is None:
        delete_markers = DEFAULT_MARKERS

    # Identify keys to delete
    delete_targetkeys = []
    for key in override_config.keys():
        for marker in delete_markers:
            if key.startswith(marker):
                delete_targetkeys.append(key[len(marker):])
                break

    # Exclude target keys from base configuration
    merged = {
        key: value
        for key, value in base_config.items()
        if key not in delete_targetkeys
    }

    # Process override configuration
    for key, value in override_config.items():
        # Skip keys with deletion markers
        is_delete_marker_key = any(key.startswith(marker) for marker in delete_markers)
        if is_delete_marker_key:
            continue

        # Process list values with deletion markers
        if isinstance(value, list):
            delete_items = []
            keep_items = []

            for item in value:
                if isinstance(item, str):
                    # Check for deletion markers
                    is_delete = False
                    for marker in delete_markers:
                        if item.startswith(marker):
                            # Add value without marker to deletion list
                            delete_items.append(item[len(marker):])
                            is_delete = True
                            break

                    if not is_delete:
                        keep_items.append(item)
                else:
                    keep_items.append(item)

            # Merge lists if the key exists in base_config
            if key in merged and isinstance(merged[key], list):
                # Remove deletion targets from base_config list
                base_items = [
                    item for item in merged[key]
                    if item not in delete_items
                ]
                # Add new items while maintaining order and preventing duplicates
                seen = set(base_items)
                for item in keep_items:
                    if item not in seen:
                        base_items.append(item)
                        seen.add(item)
                merged[key] = base_items
            else:
                # For new keys, remove duplicates
                seen = set()
                unique_items = []
                for item in keep_items:
                    if item not in seen:
                        unique_items.append(item)
                        seen.add(item)
                merged[key] = unique_items
        else:
            # Overwrite non-list values directly
            merged[key] = value

    return merged


class FilterModule(object):
    """Ansible custom filter plugin"""

    def filters(self):
        return {
            'sshd_merge_config': sshd_merge_config,
        }
