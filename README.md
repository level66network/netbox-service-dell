# netbox-service-dell
## Dell Support Service APIs
You need to request access to the Dell Warranty Status API to be able to make API calls. More information can be found [here](https://techdirect.dell.com/portal.30/Login.aspx).
## NetBox
### Preparation
#### Custom fields
You need to create two custom fields and attatch them to the object type dcim > device. This formular can be found under Username > Admin > Extras > Custom fields.
* service_until / Date
* service_type / Text
#### API access
You need to create a User Token with read and write access. This option can be found under Username > Profile > API Tokens > Add a token.
## Python
* pip3 install requests
