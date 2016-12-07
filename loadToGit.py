#!coding=UTF-8    
from BaseHTTPServer import BaseHTTPRequestHandler
import SocketServer
import io,shutil,urllib,os     

    
class MyHttpHandler(BaseHTTPRequestHandler):    
    def do_GET(self):     
        name="World"    
        issue_no = 716
	if '?' in self.path:#如果带有参数     
            self.queryString=urllib.unquote(self.path.split('?',1)[1])     
            #name=str(bytes(params['name'][0],'GBK'),'utf-8')     
            #params=urllib.parse_qs(self.queryString)     
            #print(params)     
            #name=params["name"][0] if "name" in params else None     
            name = self.queryString.split('=')[1]
	
            for i in range(0, len(pagenames)):
                if pagenames[i] == name:
			issue_no = issue_no+i
        #r_str="<a href='https://github.com/tjworks/docs/issues/" + str(issue_no)+"'>open the issue</a>"
	r_str='''
        <html>
        <head>
        <script language="JavaScript">
           window.location.href="https://github.com/tjworks/docs/issues/'''+str(issue_no)+''' "
        </script>
        </head>
	<body>
           test
	</body>
        </html>
        '''
        enc="UTF-8"    
        encoded = ''.join(r_str).encode(enc)     
        f = io.BytesIO()     
        f.write(encoded)     
        f.seek(0)     
        self.send_response(200)     
        self.send_header("Content-type", "text/html; charset=%s" % enc)     
        self.send_header("Content-Length", str(len(encoded)))     
        self.end_headers()     
        shutil.copyfileobj(f,self.wfile)     
    def do_POST(self):     
        s=str(self.rfile.readline(),'UTF-8')#先解码     
        print(urllib.parse.parse_qs(urllib.parse.unquote(s)))#解释参数     
        self.send_response(301)#URL跳转     
        self.send_header("Location", "/?"+s)     
        self.end_headers()     
 
pagenames = ["installation","administration/install-on-linux","tutorial/install-mongodb-on-red-hat","tutorial/install-mongodb-on-suse","tutorial/install-mongodb-on-amazon","tutorial/install-mongodb-on-ubuntu","tutorial/install-mongodb-on-debian","tutorial/install-mongodb-on-linux","tutorial/install-mongodb-on-os-x","tutorial/install-mongodb-on-windows","administration/install-enterprise","tutorial/install-mongodb-enterprise-on-red-hat","tutorial/install-mongodb-enterprise-on-ubuntu","tutorial/install-mongodb-enterprise-on-debian","tutorial/install-mongodb-enterprise-on-suse","tutorial/install-mongodb-enterprise-on-amazon","tutorial/install-mongodb-enterprise-on-linux","tutorial/install-mongodb-enterprise-on-windows","tutorial/verify-mongodb-packages","crud","core/crud-introduction","core/crud","core/read-operations","core/read-operations-introduction","core/cursors","core/query-optimization","core/query-plans","core/distributed-queries","core/write-operations","core/write-operations-introduction","core/write-operations-atomicity","core/distributed-write-operations","core/write-performance","core/bulk-write-operations","core/read-isolation-consistency-recency","applications/crud","tutorial/insert-documents","tutorial/query-documents","tutorial/modify-documents","tutorial/remove-documents","tutorial/project-fields-from-query-results","tutorial/limit-number-of-elements-in-updated-array","tutorial/iterate-a-cursor","tutorial/analyze-query-plan","tutorial/perform-two-phase-commits","tutorial/update-if-current","tutorial/create-tailable-cursor","tutorial/create-an-auto-incrementing-field","reference/crud","reference/write-concern","reference/readConcern","reference/sql-comparison","reference/bios-example-collection","data-modeling","core/data-modeling-introduction","core/document-validation","core/data-models","core/data-model-design","core/data-model-operations","core/gridfs","applications/data-models","applications/data-models-relationships","tutorial/model-embedded-one-to-one-relationships-between-documents","tutorial/model-embedded-one-to-many-relationships-between-documents","tutorial/model-referenced-one-to-many-relationships-between-documents","applications/data-models-tree-structures","tutorial/model-tree-structures-with-parent-references","tutorial/model-tree-structures-with-child-references","tutorial/model-tree-structures-with-ancestors-array","tutorial/model-tree-structures-with-materialized-paths","tutorial/model-tree-structures-with-nested-sets","applications/data-models-applications","tutorial/model-data-for-atomic-operations","tutorial/model-data-for-keyword-search","tutorial/model-monetary-data","tutorial/model-time-data","reference/data-models","core/document","reference/database-references","reference/gridfs","reference/object-id","reference/bson-types","administration","core/administration","administration/strategy","core/backups","administration/monitoring","administration/configuration","administration/production-notes","administration/data-management","data-center-awareness","core/operational-segregation","core/capped-collections","tutorial/expire-data","administration/optimization","administration/analyzing-mongodb-performance","tutorial/evaluate-operation-performance","tutorial/optimize-query-performance-with-indexes-and-projections","applications/design-notes","administration/tutorials","administration/maintenance","tutorial/transparent-huge-pages","tutorial/use-database-commands","tutorial/manage-mongodb-processes","tutorial/terminate-running-operations","tutorial/manage-the-database-profiler","tutorial/rotate-log-files","tutorial/manage-journaling","tutorial/store-javascript-function-on-server","tutorial/upgrade-revision","tutorial/monitor-with-snmp","tutorial/monitor-with-snmp-on-windows","tutorial/troubleshoot-snmp","administration/backup","tutorial/backup-with-filesystem-snapshots","tutorial/restore-replica-set-from-backup","tutorial/backup-and-restore-tools","administration/backup-sharded-clusters","tutorial/backup-small-sharded-cluster-with-mongodump","tutorial/backup-sharded-cluster-with-filesystem-snapshots","tutorial/backup-sharded-cluster-with-database-dumps","tutorial/schedule-backup-window-for-shardedlclusters","tutorial/restore-single-shard","tutorial/restore-sharded-cluster","tutorial/recover-data-following-unexpected-shutdown","administration/scripting","core/server-side-javascript","core/shell-types","tutorial/write-scripts-for-the-mongo-shell","tutorial/getting-started-with-the-mongo-shell","tutorial/access-mongo-shell-help","reference/mongo-shell","tutorial","reference/administration","reference/ulimit","reference/system-collections","reference/database-profiler","reference/server-status","core/journaling","reference/exit-codes","administration/production-checklist","administration/production-checklist-operations","administration/production-checklist-development","security","administration/security-checklist","core/authentication","core/security-users","core/authentication-mechanisms","core/security-scram-sha-1","core/security-mongodb-cr","core/security-x.509","core/authentication-mechanisms-enterprise","core/kerberos","core/security-ldap","core/security-internal-authentication","core/authorization","core/security-built-in-roles","core/security-user-defined-roles","core/collection-level-access-control","core/security-encryption","core/security-transport-encryption","core/security-encryption-at-rest","core/auditing","core/security-hardening","core/security-mongodb-configuration","core/security-network","administration/security","administration/security-access-control","tutorial/enable-authentication","tutorial/enable-internal-authentication","administration/security-authentication-mechanisms","tutorial/configure-x509-client-authentication","tutorial/configure-x509-member-authentication","tutorial/upgrade-keyfile-to-x509","tutorial/control-access-to-mongodb-with-kerberos-authentication","tutorial/control-access-to-mongodb-windows-with-kerberos-authentication","tutorial/troubleshoot-kerberos","tutorial/configure-ldap-sasl-activedirectory","tutorial/configure-ldap-sasl-openldap","administration/security-user-role-management","tutorial/manage-users-and-roles","tutorial/change-own-password-and-custom-data","administration/security-network","tutorial/configure-ssl","tutorial/configure-ssl-clients","tutorial/upgrade-cluster-to-ssl","tutorial/configure-fips","tutorial/configure-linux-iptables-firewall","tutorial/configure-windows-netsh-firewall","administration/security-encryption","tutorial/configure-encryption","tutorial/rotate-encryption-key","administration/security-auditing","tutorial/configure-auditing","tutorial/configure-audit-filters","administration/security-misc","tutorial/implement-field-level-redaction","tutorial/create-a-vulnerability-report","reference/security","reference/built-in-roles","reference/system-roles-collection","reference/system-users-collection","reference/resource-document","reference/privilege-actions","reference/audit-message","aggregation","core/aggregation-introduction","core/aggregation","core/aggregation-pipeline","core/map-reduce","core/single-purpose-aggregation","core/aggregation-mechanics","core/aggregation-pipeline-optimization","core/aggregation-pipeline-limits","core/aggregation-pipeline-sharded-collections","core/map-reduce-sharded-collections","core/map-reduce-concurrency","applications/aggregation","tutorial/aggregation-zip-code-data-set","tutorial/aggregation-with-user-preference-data","tutorial/map-reduce-examples","tutorial/perform-incremental-map-reduce","tutorial/troubleshoot-map-function","tutorial/troubleshoot-reduce-function","reference/aggregation","meta/aggregation-quick-reference","reference/aggregation-commands-comparison","reference/sql-aggregation-comparison","reference/operator/aggregation/interface","reference/aggregation-variables","indexes","core/indexes-introduction","core/indexes","core/index-types","core/index-single","core/index-compound","core/index-multikey","applications/geospatial-indexes","core/2dsphere","core/2d","core/geohaystack","core/geospatial-indexes","core/index-text","core/index-hashed","core/index-properties","core/index-ttl","core/index-unique","core/index-partial","core/index-sparse","core/index-creation","core/index-intersection","core/multikey-index-bounds","administration/indexes","administration/indexes-creation","tutorial/create-an-index","tutorial/create-a-compound-index","tutorial/create-a-unique-index","tutorial/create-a-partial-index","tutorial/create-a-sparse-index","tutorial/create-a-hashed-index","tutorial/build-indexes-on-replica-sets","tutorial/build-indexes-in-the-background","tutorial/roll-back-to-v1.8-index","administration/indexes-management","tutorial/remove-indexes","tutorial/modify-an-index","tutorial/rebuild-indexes","tutorial/manage-in-progress-indexing-operations","tutorial/list-indexes","tutorial/measure-index-use","administration/indexes-geo","tutorial/geospatial-tutorial","tutorial/build-a-2dsphere-index","tutorial/query-a-2dsphere-index","tutorial/build-a-2d-index","tutorial/query-a-2d-index","tutorial/build-a-geohaystack-index","tutorial/query-a-geohaystack-index","tutorial/calculate-distances-using-spherical-geometry-with-2d-geospatial-indexes","administration/indexes-text","tutorial/create-text-index-on-multiple-fields","tutorial/specify-language-for-text-index","tutorial/text-search-with-rlp","tutorial/avoid-text-index-name-limit","tutorial/control-results-of-text-search","tutorial/limit-number-of-items-scanned-for-text-search","tutorial/text-search-in-aggregation","applications/indexes","tutorial/create-indexes-to-support-queries","tutorial/sort-results-with-indexes","tutorial/ensure-indexes-fit-ram","tutorial/create-queries-that-ensure-selectivity","reference/indexes","reference/geojson","reference/text-search-languages","storage","core/mmapv1","core/wiredtiger","core/inmemory","replication","core/replication-introduction","core/replication","core/replica-set-members","core/replica-set-primary","core/replica-set-secondary","core/replica-set-priority-0-member","core/replica-set-hidden-member","core/replica-set-delayed-member","core/replica-set-arbiter","core/replica-set-architectures","core/replica-set-architecture-three-members","core/replica-set-architecture-four-members","core/replica-set-architecture-geographically-distributed","core/replica-set-high-availability","core/replica-set-elections","core/replica-set-rollbacks","applications/replication","core/replica-set-write-concern","core/read-preference","core/read-preference-mechanics","core/replication-process","core/replica-set-oplog","core/replica-set-sync","core/master-slave","administration/replica-sets","administration/replica-set-deployment","tutorial/deploy-replica-set","tutorial/deploy-replica-set-for-testing","tutorial/deploy-geographically-distributed-replica-set","tutorial/add-replica-set-arbiter","tutorial/convert-standalone-to-replica-set","tutorial/expand-replica-set","tutorial/remove-replica-set-member","tutorial/replace-replica-set-member","administration/replica-set-member-configuration","tutorial/adjust-replica-set-member-priority","tutorial/configure-secondary-only-replica-set-member","tutorial/configure-a-hidden-replica-set-member","tutorial/configure-a-delayed-replica-set-member","tutorial/configure-a-non-voting-replica-set-member","tutorial/convert-secondary-into-arbiter","administration/replica-set-maintenance","tutorial/change-oplog-size","tutorial/perform-maintence-on-replica-set-members","tutorial/force-member-to-be-primary","tutorial/resync-replica-set-member","tutorial/configure-replica-set-tag-sets","tutorial/reconfigure-replica-set-with-unavailable-members","tutorial/manage-chained-replication","tutorial/change-hostnames-in-a-replica-set","tutorial/configure-replica-set-secondary-sync-target","tutorial/troubleshoot-replica-sets","reference/replication","reference/replica-configuration","reference/local-database","reference/replica-states","reference/read-preference","sharding","core/sharding-introduction","core/sharding","core/sharded-cluster-components","core/sharded-cluster-shards","core/sharded-cluster-config-servers","core/sharded-cluster-architectures","core/sharded-cluster-requirements","core/sharded-cluster-architectures-production","core/sharded-cluster-architectures-test","core/sharded-cluster-operations","core/sharding-shard-key","core/sharded-cluster-high-availability","core/sharded-cluster-query-router","core/tag-aware-sharding","core/sharded-cluster-mechanics","core/sharding-balancing","core/sharding-chunk-migration","core/sharding-chunk-splitting","core/sharding-shard-key-indexes","core/sharded-cluster-metadata","administration/sharded-clusters","administration/sharded-cluster-deployment","tutorial/deploy-shard-cluster","tutorial/choose-a-shard-key","tutorial/shard-collection-with-a-hashed-shard-key","tutorial/add-shards-to-shard-cluster","tutorial/convert-replica-set-to-replicated-shard-cluster","tutorial/upgrade-config-servers-to-replica-set","tutorial/convert-sharded-cluster-to-replica-set","administration/sharded-cluster-maintenance","tutorial/view-sharded-cluster-configuration","tutorial/replace-config-server","tutorial/migrate-config-servers-with-same-hostname","tutorial/migrate-config-servers-with-different-hostnames","tutorial/migrate-sharded-cluster-to-new-hardware","tutorial/backup-sharded-cluster-metadata","tutorial/configure-sharded-cluster-balancer","tutorial/manage-sharded-cluster-balancer","tutorial/remove-shards-from-cluster","administration/sharded-cluster-data","tutorial/create-chunks-in-sharded-cluster","tutorial/split-chunks-in-sharded-cluster","tutorial/migrate-chunks-in-sharded-cluster","tutorial/merge-chunks-in-sharded-cluster","tutorial/modify-chunk-size-in-sharded-cluster","tutorial/clear-jumbo-flag","tutorial/administer-shard-tags","tutorial/enforce-unique-keys-for-sharded-collections","tutorial/shard-gridfs-data","tutorial/troubleshoot-sharded-clusters","reference/sharding","reference/config-database","faq","faq/fundamentals","faq/developers","faq/mongo","faq/concurrency","faq/sharding","faq/replica-sets","faq/storage","faq/indexes","faq/diagnostics","release-notes","release-notes/3.2","release-notes/3.2-changelog","release-notes/3.2-compatibility","release-notes/3.2-javascript","release-notes/3.2-upgrade","release-notes/3.2-downgrade","release-notes/3.0","release-notes/3.0-changelog","release-notes/3.0-compatibility","release-notes/3.0-upgrade","release-notes/3.0-scram","release-notes/3.0-downgrade","release-notes/2.6","release-notes/2.6-changelog","release-notes/2.6-compatibility","release-notes/2.6-upgrade","release-notes/2.6-upgrade-authorization","release-notes/2.6-downgrade","release-notes/2.4","release-notes/2.4-changelog","release-notes/2.4-javascript","release-notes/2.4-upgrade","release-notes/2.4-index-types","release-notes/2.2","release-notes/2.0","release-notes/1.8","release-notes/1.6","release-notes/1.4","release-notes/1.2","products","products/ops-manager","products/cloud-manager","products/compass","products/bi-connector","contributors","contributors/getting-started","contributors/tutorial/choose-a-project","contributors/tutorial/choose-a-jira-ticket","contributors/tutorial/set-up-a-github-fork","contributors/tutorial/submit-a-github-pull-request","contributors/core/style-guidelines","contributors/reference/resources-for-contributors","contributors/drivers","contributors/core/drivers","contributors/reference/drivers","contributors/reference/drivers-style-guidelines","contributors/server-guidelines","contributors/reference/server-design-guidelines","contributors/reference/server-code-style","contributors/reference/server-exception-architecture","contributors/reference/server-string-manipulation","contributors/reference/server-logging-rules","contributors/reference/server-memory-management","contributors/reference/durability-internals","contributors/server-resources","contributors/tutorial/build-mongodb-from-source","contributors/tutorial/build-tools-from-source","contributors/tutorial/write-tests-for-server-code","contributors/tutorial/test-the-mongodb-server","contributors/reference/parsing-stack-traces","contributors/reference/js-benchmarking-harness","index"]

httpd=SocketServer.TCPServer(('',8080),MyHttpHandler)     
print("Server started on 127.0.0.1,port 8080.....")     
httpd.serve_forever()