for type in 'thread' 'process';
	    do
		for i in {1..20}; do
		    echo "$type: $i";
		    echo "$type: $i" >> stats.txt
		    python prime_check_process.py $i thread | grep -vi checking >> stats.txt;
		done;
	done
