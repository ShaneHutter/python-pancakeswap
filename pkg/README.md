# PKG files
This directory contains various PKGBUILDs for various distributions

## Debian
For Debian packages insall python3-stdeb
```
apt install -y python3-stdeb
```

The following will build a DEB
```
./setup.py sdist && \
./setup.py --command-packages=stdeb.command bdist_deb && \
./setup.py clean
```

## RHEL
You can use the buit in RPM builder in distutils to build an RPM
```
./setup.py bdist_rpm
```

## Additional Notes
Current instructions above will be improved, and further instructions for other distributions will be provided at a later date.