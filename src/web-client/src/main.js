'use strict';

const e = React.createElement;

class SimplyMLRequestForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
			data: {
				value: "{\n  'data':'test'\n}",
				rows: 3
			},
			options: {
				value: "{\n  'options':'test'\n}",
				rows: 3
			}
		};

    this.handleDataChange = this.handleDataChange.bind(this);
		this.handleOptionsChange = this.handleOptionsChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleDataChange(event) {
    this.setState({
			data: {
				value: event.target.value,
				rows: event.target.value.split(/\r\n|\r|\n/).length
			}
		});
  }

	handleOptionsChange(event) {
		this.setState({
			options: {
				value: event.target.value,
				rows: event.target.value.split(/\r\n|\r|\n/).length
			}
		});
	}

  handleSubmit(event) {
    alert('Data was submitted: ' + this.state.data.value);
		alert('With these options: ' + this.state.options.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>

        <div class="flex-container">

        <div>
					<textarea
						value={this.state.data.value}
						onChange={this.handleDataChange}
						rows={this.state.data.rows}
					/>	
        </div>

        <div>
					<textarea 
						value={this.state.options.value}
						onChange={this.handleOptionsChange} 
						rows={this.state.options.rows}
					/>
        </div>

        <div>
          <input type="submit" value="Submit" />
        </div>

        </div>

      </form>
    );
  }
}

const domContainer = document.querySelector('#request_form_container');
ReactDOM.render(e(SimplyMLRequestForm), domContainer);
