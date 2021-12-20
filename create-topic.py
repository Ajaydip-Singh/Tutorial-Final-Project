from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9093", 
    client_id='test'
)

test_topic = []
test_topic.append(NewTopic(name="test-topic", num_partitions=3, replication_factor=3))
admin_client.create_topics(new_topics=test_topic, validate_only=False)
