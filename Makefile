build-db:
	docker build db/. -t db
run-db:
	docker run --name db -d db
exec-db:
	docker exec -it db mariadb -p
sh-db:
	docker exec -it db sh
rm-db:
	docker stop db
	docker rm db