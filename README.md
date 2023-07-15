---
# Ansible Role: sshd

## Description

Manage OpenSSH client and server configrations.

## Installation

```
ansible-galaxy install autechgemz.sshd
```

## Requirements

None

## Dependencies

None

## Example Playbook

```
- hosts: all
  roles:
    - autechgemz.sshd
```

## Role Variables

### sshd_debug

```
sshd_debug: false
```

### sshd_package_ensure
```
sshd_package_ensure: 'present'
```

### sshd_service_ensure
```
sshd_service_ensure: 'started'
```

### sshd_service_enable:
```
sshd_service_enable: true
```

### sshd_daemon_config_options
```
sshd_daemon_config_options:
```

### sshd_client_config_options
```
sshd_client_config_options:
  Host:
    - pattern: '*'
      keywords:
        GSSAPIAuthentication: 'yes'
        ForwardX11Trusted: 'yes'
    - pattern: '*'
      keywords:
        GSSAPIAuthentication: 'no'
        ForwardX11Trusted: 'no'
        SendEnv:
          - 'LANG LC_CTYPE LC_NUMERIC LC_TIME LC_COLLATE LC_MONETARY LC_MESSAGES'
          - 'LC_PAPER LC_NAME LC_ADDRESS LC_TELEPHONE LC_MEASUREMENT'
          - 'LC_IDENTIFICATION LC_ALL LANGUAGE XMODIFIERS'
```

### sshd_server_config_options
```
sshd_server_config_options:
  AddressFamily: 'inet'
  HostKey:
    - '/etc/ssh/ssh_host_rsa_key'
    - '/etc/ssh/ssh_host_ecdsa_key'
    - '/etc/ssh/ssh_host_ed25519_key'
  SyslogFacility: 'AUTHPRIV'
  AuthorizedKeysFile: '.ssh/authorized_keys'
  PasswordAuthentication: 'no'
  ChallengeResponseAuthentication: 'no'
  GSSAPIAuthentication: 'yes'
  GSSAPICleanupCredentials: 'no'
  UsePAM: 'yes'
  X11Forwarding: 'no'
  AcceptEnv:
    - 'LANG LC_CTYPE LC_NUMERIC LC_TIME LC_COLLATE LC_MONETARY LC_MESSAGES'
    - 'LC_PAPER LC_NAME LC_ADDRESS LC_TELEPHONE LC_MEASUREMENT'
    - 'LC_IDENTIFICATION LC_ALL LANGUAGE XMODIFIERS'
  AuthorizedKeysCommand: "/usr/bin/sss_ssh_authorizedkeys"
  AuthorizedKeysCommandUser: "root"
  Banner: 'none'
  PrintMotd: 'no'
  Match:
    - criteria: 'Group'
      pattern: 'admin-guys'
      keywords:
        PasswordAuthentication: 'yes'
    - criteria: 'User'
      pattern: 'bobs'
      keywords:
        PasswordAuthentication: 'yes'
```

### sshd_client_dropin_config_options

```
sshd_client_dropin_config_options: []
```

### sshd_client_dropin_config_purge

```
sshd_client_dropin_config_purge: false
```

### sshd_server_dropin_config_options

```
sshd_server_dropin_config_options: []
```

### sshd_server_dropin_config_purge

```
sshd_server_dropin_config_purge: false
```

### sshd_dropin_config_manage

```
sshd_dropin_config_manage: false
```

### sshd_moduli_secure

```
sshd_moduli_secure: true
```

## Example vars

```
sshd_server_config_options:
  Protocol: '2'
  PermitRootLogin: 'no'
  PasswordAuthentication: 'no'
  PermitEmptyPasswords: 'no'
  ChallengeResponseAuthentication: 'no'
  UsePAM: 'no'
  UseDNS: 'no'
  AcceptEnv:
    - 'LANG LC_*'
  SyslogFacility: 'AUTHPRIV'
  LogLevel: 'VERBOSE'
  IgnoreRhosts: 'yes'
  Subsystem: ""
  X11Forwarding: 'no'
  ListenAddress: '0.0.0.0'
  PubkeyAuthentication: 'yes'
  GSSAPIAuthentication: 'no'
  GSSAPICleanupCredentials: 'no'
  PrintMotd: 'no'
  MaxStartups: '3'
  HostKey:
    - /etc/ssh/ssh_host_ed25519_key
    - /etc/ssh/ssh_host_rsa_key
  Ciphers: chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
  KexAlgorithms: sntrup761x25519-sha512@openssh.com,curve25519-sha256,curve25519-sha256@libssh.org,gss-curve25519-sha256-,diffie-hellman-group16-sha512,gss-group16-sha512-,diffie-hellman-group18-sha512,diffie-hellman-group-exchange-sha256
  MACs: hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,umac-128-etm@openssh.com
  HostKeyAlgorithms: ssh-ed25519,ssh-ed25519-cert-v01@openssh.com,sk-ssh-ed25519@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,rsa-sha2-512,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256,rsa-sha2-256-cert-v01@openssh.com
```

## License

This role is under the MIT License. See the LICENSE file for the full license text.