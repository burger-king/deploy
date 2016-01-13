# Deploy a bk server

Copy `hosts.ini.sample` to `hosts.ini` and edit it to your liking.

Then run:

    ./deploy.sh <ENV NAME>

where `<ENV NAME>` is one of `development, production`.

This will install `ansible` if it is not present on your system.
