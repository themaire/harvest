#!/usr/bin/python3
# -*- coding: utf-8 -*-

##### Modules #####

# Database
import pymysql.cursors

##### Functions #####

def queryInsert(param1, param2, param3):
	"""
	Build your own insert query
	
	param@param1 : the table name
	param@param2 : the field name
	param@param3 : the data value
	
	return : you cooked query :-)
	"""
	
	query = "INSERT INTO `{param1}` (param2) VALUES ({param3})".format(param1=param1, param2=param2, param3=param3)
	return query

# ---->

# test of queryInsert() to see what happens
if __name__ == "__main__":
	try:
		print('queryInsert("temperature", "temp_temp", 12.5)\n' + queryInsert("temperature", "tem_temp", 12.5))
		print()
		print('queryInsert("light", "lig_light", 2000)\n' + queryInsert("light", "lig_light", 2000))

	except KeyboardInterrupt:
		exit()