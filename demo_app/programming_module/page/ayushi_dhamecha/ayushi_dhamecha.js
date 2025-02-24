frappe.pages['ayushi-dhamecha'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Welcome to frappe world !!',
		single_column: true
	});
	page.set_title('My Page')
	page.set_title_sub('Subtitle')
	page.set_indicator('Pending', 'orange')
	// page.clear_indicator()
	let $btn = page.set_primary_action('New', () => frappe.msgprint('Primary action button clicked'), 'octicon octicon-plus')
	// page.clear_primary_action()

	let $btn2 = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync')
	// page.add_menu_item('Send Email', () => open_email_dialog())
	page.add_menu_item('Send Email', () => open_email_dialog(), true)
	page.add_action_item('Delete', () => delete_items())
	page.add_inner_button('Update Posts', () => update_posts())

	page.add_inner_button('New Post', () => new_post(), 'Make')


	let field = page.add_field({
		label: 'Status',
		fieldtype: 'Select',
		fieldname: 'status',
		options: [
			'Open',
			'Closed',
			'Cancelled'
		],
		change() {
			console.log(field.get_value());
		}
	});

// --------------------------------------------Chart API--------------------------------------------------
	$(page.main).append('<div id="chart-container"></div>');
	frappe.call({
        method: 'demo_app.API.chart_API.get_chart_data',
        callback: function(response) {
            if (response.message) {
                render_chart(response.message);
            }
        }
    });
}


let values = page.get_form_values()
	console.log(values)

	
// ------------------------------------------chart---------------------------------------------
	function render_chart(data) {
		const chart = new frappe.Chart('#chart-container', {
			title: 'Sales Orders Over Time',
			data: data,
			type: 'bar', // 'line', 'bar', 'pie', 'percentage'
			height: 250,
			colors: ['#7cd6fd'],
			axisOptions: {
				xIsSeries: true
			}
		});
	}