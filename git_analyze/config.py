conf = {
	'max_domains': 10,
	'max_ext_length': 10,
	'style': 'gitstats.css',
	'max_authors': 20,
	'authors_top': 5,
	'commit_begin': '',
	'commit_end': 'HEAD',
	'linear_linestats': 1,
	'project_name': '',
	'processes': 8,
	'start_date': ''
}

key_author_format = "author"
key_commit_format = "commit"
key_deletions_format = "deletions"
key_insertions_format = "insertions"
key_file_changesformat = "file_changes"

gitConfig = {
	"projects" : [
		{
			"group": "document",
			"name": "document",
			"git_path": "http://git.51baiwang.com/baiwang/document.git"
		}
		,
		{
			"group": "client",
			"name": "client-choushu-web",
			"git_path": "http://git.51baiwang.com/baiwang/client-choushu-web.git"
		},
		{
			"group": "client",
			"name": "appstore",
			"git_path": "http://git.51baiwang.com/bigclient/appstore.git"
		},
		{
			"group": "client",
			"name": "OceanusContainer",
			"git_path": "http://git.51baiwang.com/bigclient/OceanusContainer.git"
		},
		{
			"group": "client",
			"name": "OCRContainer",
			"git_path": "http://git.51baiwang.com/bigclient/OCRContainer.git"
		},
		{
			"group": "client-server",
			"name": "client-support",
			"git_path": "http://git.51baiwang.com/baiwang/client-support.git"
		},
		{
			"group": "client-server",
			"name": "client-admin",
			"git_path": "http://git.51baiwang.com/baiwang/client-admin.git"
		},
		{
			"group": "client-server",
			"name": "client-gateway",
			"git_path": "http://git.51baiwang.com/baiwang/client-gateway.git"
		},
		{
			"group": "tax",
			"name": "media-config-service",
			"git_path": "http://git.51baiwang.com/tax/media-config-service.git"
		},
		{
			"group": "tax",
			"name": "media-bill-service",
			"git_path": "http://git.51baiwang.com/tax/media-bill-service.git"
		},
		{
			"group": "tax",
			"name": "media-basic-service",
			"git_path": "http://git.51baiwang.com/tax/media-basic-service.git"
		},
		{
			"group": "tax",
			"name": "ocr-api",
			"git_path": "http://git.51baiwang.com/mobile/ocr-api.git"
		},
		{
			"group": "juno",
			"name": "juno-manage-service",
			"git_path": "http://git.51baiwang.com/juno/juno-manage-service.git"
		},
		{
			"group": "juno",
			"name": "juno-order-service",
			"git_path": "http://git.51baiwang.com/juno/juno-order-service.git"
		},
		{
			"group": "juno",
			"name": "juno-pay-service",
			"git_path": "http://git.51baiwang.com/juno/juno-pay-service.git"
		},
		{
			"group": "juno",
			"name": "juno-api",
			"git_path": "http://git.51baiwang.com/juno/juno-api.git"
		},
		{
			"group": "juno",
			"name": "juno-open-service",
			"git_path": "http://git.51baiwang.com/juno/juno-open-service.git"
		},
		{
			"group": "juno",
			"name": "juno-push-service",
			"git_path": "http://git.51baiwang.com/juno/juno-push-service.git"
		},
		{
			"group": "juno",
			"name": "juno-push-api",
			"git_path": "http://git.51baiwang.com/juno/juno-push-api.git"
		},
		{
			"group": "zeus",
			"name": "contract-api",
			"git_path": "http://git.51baiwang.com/zeus/contract-api.git"
		},
		{
			"group": "zeus",
			"name": "contract-service",
			"git_path": "http://git.51baiwang.com/zeus/contract-service.git"
		},
		{
			"group": "zeus",
			"name": "zeus-user-service",
			"git_path": "http://git.51baiwang.com/zeus/zeus-user-service.git"
		},
		{
			"group": "openplatform",
			"name": "dunit-proxy",
			"git_path": "http://git.51baiwang.com/deviceovercloud/dunit-proxy.git"
		},
		{
			"group": "openplatform",
			"name": "baiwang-doc-sdk",
			"git_path": "http://git.51baiwang.com/deviceovercloud/baiwang-doc-sdk.git"
		},
		{
			"group": "openplatform",
			"name": "doc-common",
			"git_path": "http://git.51baiwang.com/deviceovercloud/doc-common.git"
		},
		{
			"group": "openplatform",
			"name": "dunit-proxy",
			"git_path": "http://git.51baiwang.com/deviceovercloud/dunit-proxy.git"
		},
		{
			"group": "openplatform",
			"name": "admin-portal",
			"git_path": "http://git.51baiwang.com/baiwang/admin-portal.git"
		},
		{
			"group": "openplatform",
			"name": "athena-api",
			"git_path": "http://git.51baiwang.com/baiwang/athena-api.git"
		},
		{
			"group": "openplatform",
			"name": "athena-sdk",
			"git_path": "http://git.51baiwang.com/baiwang/athena-sdk.git"
		},
		{
			"group": "openplatform",
			"name": "athena-timer",
			"git_path": "http://git.51baiwang.com/baiwang/athena-timer.git"
		},
		{
			"group": "openplatform",
			"name": "athena-common",
			"git_path": "http://git.51baiwang.com/baiwang/athena-common.git"
		},
		{
			"group": "openplatform",
			"name": "sdk-java",
			"git_path": "http://git.51baiwang.com/baiwang/sdk-java.git"
		},
		{
			"group": "openplatform",
			"name": "open-isp-service",
			"git_path": "http://git.51baiwang.com/baiwang/open-isp-service.git"
		},
		{
			"group": "openplatform",
			"name": "doorman-service",
			"git_path": "http://git.51baiwang.com/baiwang/doorman-service.git"
		},
		{
			"group": "openplatform",
			"name": "app-service",
			"git_path": "http://git.51baiwang.com/baiwang/app-service.git"
		},
		{
			"group": "openplatform",
			"name": "magpie-gateway",
			"git_path": "http://git.51baiwang.com/baiwang/magpie-gateway.git"
		},
		{
			"group": "openplatform",
			"name": "baiwang-bigcustomersdk",
			"git_path": "http://git.51baiwang.com/baiwang/baiwang-bigcustomersdk.git"
		},
		{
			"group": "openplatform",
			"name": "openplatform-sdk-java-new",
			"git_path": "http://git.51baiwang.com/baiwang/openplatform-sdk-java-new.git"
		},
		{
			"group": "openplatform",
			"name": "magpie-common",
			"git_path": "http://git.51baiwang.com/baiwang/magpie-common.git"
		},
		{
			"group": "openplatform",
			"name": "mananger-platform",
			"git_path": "http://git.51baiwang.com/baiwang/mananger-platform.git"
		},
		{
			"group": "openplatform",
			"name": "BopSDKUtil",
			"git_path": "http://git.51baiwang.com/baiwang/BopSDKUtil.git"
		},
		{
			"group": "openplatform",
			"name": "tax-control-dms",
			"git_path": "http://git.51baiwang.com/baiwang/tax-control-dms.git"
		},
		{
			"group": "openplatform",
			"name": "bop-manage",
			"git_path": "http://git.51baiwang.com/baiwang/bop-manage.git"
		},
		{
			"group": "openplatform",
			"name": "others-service",
			"git_path": "http://git.51baiwang.com/baiwang/others-service.git"
		},
		{
			"group": "openplatform",
			"name": "user-service",
			"git_path": "http://git.51baiwang.com/baiwang/user-service.git"
		},
		{
			"group": "openplatform",
			"name": "support-service",
			"git_path": "http://git.51baiwang.com/baiwang/support-service.git"
		}
	]
}

